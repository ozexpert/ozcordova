starterModule.controller("globalCtrl", function($scope){
	$scope.meta = {
		backgroundMode: false,
		backgroundService: false
	};

	$scope.$watch('meta.backgroundMode', function(newVal, oldVal){
		if(typeof cordova != 'undefined'){
			if(newVal){
				cordova.plugins.backgroundMode.enable();
				cordova.plugins.backgroundMode.configure({ 
				  title: 'Connected',
				  ticker: 'Connected to ozcordova',
				  text:'Accelerating your web'
				});
			} else {
				cordova.plugins.backgroundMode.disable();
			}
		}
	});

	/* background service */
	var successHandler = function(data){
		if(data.ServiceRunning){
			alert('Service is running');
		} else {
			alert('Service stopped');
		}
	};

	$scope.$watch('meta.backgroundService', function(newVal, oldVal){
		if(typeof backgroundService != 'undefined'){
			if(newVal){
				backgroundService.startService(function(r){ successHandler(r); }, function(e){ alert(e); });
			} else {
				backgroundService.stopService(function(r){ successHandler(r); }, function(e){ alert(e); });
			}
		}
	});

	// myService.startService(function(r) {
 //                    handleSuccess(r)
 //                },
 //                        function(e) {
 //                            handleError(e)
 //                        });
});