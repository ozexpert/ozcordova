// Ionic Starter App

// angular.module is a global place for creating, registering and retrieving Angular modules
// 'starter' is the name of this angular module example (also set in a <body> attribute in index.html)
// the 2nd parameter is an array of 'requires'
var starterModule = angular.module('starter', ['ionic']);

starterModule.run(function($ionicPlatform) {
  $ionicPlatform.ready(function() {
    // Hide the accessory bar by default (remove this to show the accessory bar above the keyboard
    // for form inputs)
    if(window.cordova && window.cordova.plugins.Keyboard) {
      cordova.plugins.Keyboard.hideKeyboardAccessoryBar(true);
    }
    if(window.StatusBar) {
      StatusBar.styleDefault();
    }
  });
});

document.addEventListener('deviceready', function () {
    // Enable background mode
    // cordova.plugins.backgroundMode.enable();
    // Android customization
    cordova.plugins.backgroundMode.configure({ 
      title: 'Connected',
      ticker: 'tick',
      text:'Doing heavy tasks.'
    });
}, false);