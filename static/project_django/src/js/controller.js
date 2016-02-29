var app = angular.module("product-product",[]);

app.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
});

app.directive('myEnter', function () {
    return function (scope, element, attrs) {
        element.bind("keydown keypress", function (event) {
            if(event.which === 13) {
                scope.$apply(function (){
                    scope.$eval(attrs.myEnter);
                });

                event.preventDefault();
            }
        });
    };
});

app.factory('FilterListProduct',function($http){
    var FilterListProduct = {}
    FilterListProduct.product = ''

    FilterListProduct.get_prodcut = function(product_id){
        console.log(product_id)
    };

    return FilterListProduct
})

app.controller('product-controller', function($scope, FilterListProduct){
    $scope.filterProduct = 'Juan Perez Castro'
    $scope.get_prodcut = function (){
        console.log('se MEte')
        FilterListProduct.get_prodcut($scope.filterProduct)
    }


})


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