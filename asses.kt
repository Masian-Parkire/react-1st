class Artist(var name:String,var country:String,var musicalStyle:String,var instruments:String){
    fun presentArtist():String{
        return "$name $country $musicalStyle $instruments"
    }
}
open class Performance(var performingArtist:Artist,var startTime:String,var endTime:String){
    open fun perform():String{
        return "on the music performance we will have ${performingArtist.name} first and her performance will start at $startTime and end at $endTime"
    }
  class MusicPerformance(performingArtist: Artist,startTime: String,endTime: String):Performance(performingArtist, startTime, endTime){
  }
    class DancePerformance(performingArtist: Artist,startTime: String,endTime: String):Performance(performingArtist, startTime, endTime){
    }
}
open class Stage(var name: String,var capacity:Int){
    class MainStage(name: String,capacity: Int):Stage(name, capacity){
        fun performingOnStage(){
            val arrangement1= mutableListOf<Map<String,Any>>()
            val list= mutableMapOf<String,Any>()
            list["artist1"]="penroid"
            list["artist2"]="bill Gaither"
            list["artist3"]="jabidii"
            list["artist4"]="ken rodgers"
            arrangement1.add(list)
            println(arrangement1)
        }
    }
    class Stage2(name: String,capacity: Int):Stage(name, capacity){
        fun performingOnStage(){
            val arrangement2= mutableListOf<Map<String,Any>>()
            val list= mutableMapOf<String,Any>()
            list["artist1"]="penroid"
            list["artist2"]="bill Gaither"
            list["artist3"]="jabidii"
            list["artist4"]="ken rodgers"
            arrangement2.add(list)
            println(arrangement2)
        }
    }
}












