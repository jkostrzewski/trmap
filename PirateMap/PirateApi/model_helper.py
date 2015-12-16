from bson.code import Code

world_data_mapper = Code("""
               function () {
               total = 0
               this.data.forEach(function(d){
                total+=d["count"]
               	emit(d["code"], d["count"])
               	})
               }
               """)

world_data_reducer = Code("""
     			function (key, values) {
    				return Array.sum(values)
    			}
                """)

def nation_data_mapper(code):
            return Code("""
               function() {
               category = this.category
               total=0
               this.data.forEach(function(d){
                if (d["code"]==code){
                  emit(category, d["count"])
                  total+=d["count"]
                }                
                })
                emit("total", total)
               }
               """, {'code':code})

nation_data_reducer = Code("""
          function (key, values) {
          return Array.sum(values)
          }
                """)

most_pop_torr_mapper = Code("""
               function () {
               link = this.link
               this.data.forEach(function(d){
                  emit(link, d["count"])
                })
               
               }
  """)

most_pop_torr_reducer = Code("""
          function (key, values) {
            return Array.sum(values)
          }
  """)


world_data_default_coll='world_data'
nation_default_coll='nation_data'