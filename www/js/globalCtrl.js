starterModule.controller("globalCtrl", function($scope){
	$scope.meta = {
		backgroundMode: false
	};

	$scope.$watch('meta.backgroundMode', function(newVal, oldVal){
		if(typeof cordova != 'undefined'){
			if(newVal){
	    		cordova.plugins.backgroundMode.enable();
			} else {
	    		cordova.plugins.backgroundMode.disable();
			}
		}
	});
});