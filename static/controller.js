var app = angular.module("controlExample",[]);

app.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
});

app.controller("divController",function($scope,$http){
	$scope.humano = {}
	$scope.lista_humanos = []	
	$scope.agregarHumano = function (){
		$scope.lista_humanos.push($scope.humano)
		$scope.humano = {}
	}
	$scope.snippetList = function(){
			$http.get('http://localhost:8000/terminal/snippets/')
			.success(function(data){
				console.log(data)
			})
			.error(function (err){
				console.log(err)
			});
	}	

});

app.controller('divConsumAjax',function($scope, $http){
		$scope.product = {}
		$scope.snippetPost = function(){
		var product = {
						 name : $scope.product.name,
						 active: $scope.product.active	,	 
						 code: $scope.product.code,
						 type: $scope.product.type,
						 price_sale: $scope.product.price_sale,
						 qty_available: $scope.product.qty_available
					}
		$http.post('http://localhost:8000/terminal/snippets/', product)
		.success(function(data){
			console.log('success')
			console.log(data)
			$scope.product = {}
		})
		.error(function(err){
			console.log('error')
			console.log(err)
		});
	}	
})