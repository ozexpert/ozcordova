from fabric.api import local, settings
from fabric.colors import red, green, yellow
from fabric.contrib.console import prompt


PACKAGE_NAME = 'ozcordova'
DROPBOX_LOCATION = '~/Dropbox/ozcordova/'
BUILDER = 'codeinfaith'
KEYSTORE = '~/Projects/github/p4n_resource/keys/%(builder)s.keystore' % {'builder': BUILDER}
APK_LOCATION = 'platforms/android/ant-build'


def new(projectname):
    """
        [STEP 1] Start new ionic project - 'fab new:ProjectName'
    """
    local("ionic start %(projectname)s blank" % {'projectname': projectname})
    prompt(yellow("Now modify config.xml and then do 'fab add_platform'."))


def add_platform(platform='android'):
    """
        [STEP 2] Add platform - 'fab add_platform:ios' (default android)
    """
    local("ionic platform add %(platform)s" % {'platform': platform})


def start():
    """
        Run in web server
    """
    local("ionic serve")


def run(device='android'):
    """
        Run in device
    """
    local("ionic run %(device)s --device" % {'device': device})


def easytether(disable=True):
    """
        Enable/Disable EasyTether (by default it disables)
    """
    if disable:
        local("sudo kextunload /System/Library/Extensions/EasyTetherUSBEthernet.kext")
    else: 
        local("sudo kextload /System/Library/Extensions/EasyTetherUSBEthernet.kext")


def build(platform='android'):
    """
        Command to build package depending on platform (ex: fab build:ios)
    """
    local("ionic build %s" % platform)
    dropbox(platform=platform)


def dropbox(platform='android'):
    """
        Copy package file to dropbox
    """
    if platform == 'android':
        with settings(warn_only=True):
            local("cp %(apk_location)s/%(package)s-debug.apk %(dropbox)s" % {'package': PACKAGE_NAME, 'apk_location': APK_LOCATION, 'dropbox': DROPBOX_LOCATION})
            local("cp %(apk_location)s/%(package)s.apk %(dropbox)s" % {'package': PACKAGE_NAME, 'apk_location': APK_LOCATION, 'dropbox': DROPBOX_LOCATION})


def push(message):
    """
        Push changes to Git repository
    """
    local("git add --all")
    local("git commit -m '%s'" % message)
    local("git push origin master")


def release(platform='android'):
    """
        Make release
    """
    local("cordova build --release %s" % platform)
    if platform == "android":
        with settings(warn_only=True):
            local("rm %(apk_location)s/%(package)s.apk" % {'package': PACKAGE_NAME, 'apk_location': APK_LOCATION})
        local("jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1 -keystore %(keystore)s %(apk_location)s/%(package)s-release-unsigned.apk %(builder)s" % {'package': PACKAGE_NAME, 'apk_location': APK_LOCATION, 'builder': BUILDER, 'keystore': KEYSTORE})
        local("zipalign -v 4 %(apk_location)s/%(package)s-release-unsigned.apk %(apk_location)s/%(package)s.apk" % {'package': PACKAGE_NAME, 'apk_location': APK_LOCATION})
        dropbox(platform='android')


def update_cordova(update_sim='false'):
    """
        Updates cordova to the lastest possible release
    """
    local("npm update -g cordova")
    local("npm update -g plugman")
    if update_sim == 'true':
        local("npm install -g ios-sim")


def update_platform(platform='android'):
    """
        Updates platform. This needs to be performed after cordova update
    """
    local("cordova platform update %(platform)s" % {'platform': platform})


def update_ionic_cli():
    """
        Updates ionic CLI to the latest
    """
    local("sudo npm update -g ionic")


def update_ionic_lib():
    """
        Updates ionic library to the latest
    """
    local("ionic lib update")


def install_console():
    """
        Installs debug console
    """
    local("cordova plugin add org.apache.cordova.console")


def remove_console():
    """
        Removes debug console
    """
    local("cordova plugin rm org.apache.cordova.console")


def manifest(platform='android'):
    if platform == 'android':
        local("vim ./platforms/android/AndroidManifest.xml")


def config(platform='android'):
    if platform == 'android':
        local("vim ./www/config.xml")


def screenshot(url='http://127.0.0.1:8100'):
    """ generate screenshot for given url (viewportsizes.com / mockuphone.com)"""
    local("casperjs ./tools/js/screenshots.js %s" % url)


def watch():
    local("grunt watch")
