var app = angular.module('app', ['datamaps', 'ngResource']);
app.config(function($resourceProvider) {
  $resourceProvider.defaults.stripTrailingSlashes = false;
});


