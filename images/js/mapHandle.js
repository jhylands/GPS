var posMap;
var indexOfTrace = 0;
var curTrace= 0;
$.ajax('ind.json').done(function(data){posMap=eval(data);});

function showCell(value){
    document.getElementById('mapImage').style.visibility='Hidden';
    var grf = document.getElementById('graph');
    indexOfTrace = 0;
    curTrace = value;
    srcNum = posMap[value][0];
    grf.src= 'boxes/' + srcNum + '.png';
    grf.style.visibilty ='Visible';
}
function back2Som(){
    document.getElementById('mapImage').style.visibility='Visible';
    var grf = document.getElementById('graph');
    grf.style.visibilty ='Hidden';
    grf.src='';
}
function changeTrace(delta){
    indexOfTrace = indexOfTrace+delta % posMap[curTrace].length;
    srcNum = posMap[curTrace][indexOfTrace];
    var grf = document.getElementById('graph');
    grf.src= 'boxes/' + srcNum + '.png';
}
function som2(method){
    document.getElementById('mapImage').src = 'maps/' + method +'Hits.png';
}
