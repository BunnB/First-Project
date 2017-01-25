import { Event } from './event';
var key;
var data;
var array = [];
var ref = firebase.database().ref('events');
var today = new Date();
var curr_day = today.getDate(); //curr day
var _id = 0;
child id, set id path = null if passed.
ref.on('value',function(snap){
    snap.forEach(function(childSnapshot){
        key = childSnapshot;
        data = childSnapshot.val();
        //console.log(data)
        //var index = data.description.lastIndexOf(',')
        //var data_date = data.description.substr(index-2,2)
        //data_date = parseInt(data_date)
        //console.log(data_date)
        //console.log(curr_day)
        //if(data_date < curr_day+3){ref.child("id").remove()}//removes data is from yesterday
        //else{
        //array.push(JSON.stringify(Event(data)));

        array.push({
          id: _id,
          name: data.name,
          start_time: data.start_time,
          end_time: data.end_time,
          location: data.location,
          lat: data.lat,
          lng: data.lng,
          description: data.description,
        });
        _id = _id + 1
      });
    });

        //array.push(dict.toString());
    //data = snap.exportVal();
   //});
console.log(JSON.stringify(array));

export const EVENTS: Event[] = [
    { id: 0, name: "MLH Local Hack Day", start_time: "9:00AM", end_time: "9:00PM", location: "sci center", lat: 37.5, lng: 75, description: " " }
];
