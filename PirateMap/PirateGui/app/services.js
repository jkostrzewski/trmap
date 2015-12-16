app.factory('worldData', function($resource){
    return $resource('http://localhost:8000/api/world_data/', {}, {
        get: { method: 'GET'},
        create: { method: 'POST' }
    })

	});

app.factory('nationData', function($resource){
    return $resource('http://localhost:8000/api/nation_data/:id/', {}, {
        get: { method: 'GET'},
        create: { method: 'POST' }
    })

	});