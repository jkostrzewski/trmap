app.controller('PirateCtrl', function($scope, worldData, nationData) {


      $scope.plugins = {
      };


       $scope.map = {
        scope: 'world',
        responsive: true,
        projection:'equirectangular',
        options: {
          staticGeoData: true
        },
        dataUrl:'app/defaultCountryData.json',
        geographyConfig: {
        
          highlightBorderColor: '#bada55',
          popupTemplate: function(geography, data) {
            return '<div class="hoverinfo">' +
                     geography.properties.name +
                     '<br>Torrents: ' +
                     (data.tn || '0') +
                   '</div>';
          },
          highlightBorderWidth: 3
        }
        ,
        fills: {
          '0':'rgba(0, 0, 255, 0.05)',
          '1':'rgba(0, 0, 255, 0.1)',
          '2':'rgba(0, 0, 255, 0.2)',
          '3':'rgba(0, 0, 255, 0.3)',
          '4':'rgba(0, 0, 255, 0.4)',
          '5':'rgba(0, 0, 255, 0.5)',
          '6':'rgba(0, 0, 255, 0.6)',
          '7':'rgba(0, 0, 255, 0.7)',
          '8':'rgba(0, 0, 255, 0.8)',
          '9':'rgba(0, 0, 255, 0.9)',
          '10':'rgba(0, 0, 255, 1)',
          'd':'rgba(0, 0, 255, 0.05)',
          defaultFill: 'rgba(0, 0, 255, 0.05)'
        },
        data:{}
        
      }
      $scope.getNationDetails = function(geography) {
		  nationData.get({'id':geography.id}, function(nationData){
		  	$scope.total=nationData.total
		  	$scope.games=nationData.games
		  	$scope.porn=nationData.porn
		  	$scope.movies=nationData.movies
		  	$scope.music=nationData.music
		  	$scope.applications=nationData.applications
		  	$scope.other=nationData.other
		  })
		  
	   } 

	 $scope.updateWorldMap = function(){
	 	worldData.get().$promise.then(function(r){
	 		for (var k in r){
	 		if ($scope.map.data[k]){
	 			$scope.map.data[k] = r[k]
	 		}
	 		}
	 	})
	 }
	 angular.element(document).ready(function () {
	 	$scope.updateWorldMap()	
        setInterval(function(){
	 		$scope.updateWorldMap()	
	 	}, 7000)
      });
});
