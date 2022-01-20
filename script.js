window.onload=init;

function init(){
    document.getElementById('summarize').addEventListener('click',callapi);
    function callapi(){
        var url=document.getElementById('url').value;
        console.log(url)
        var id=url.split("=")[1]
        console.log(id)
        let text={"data":[id,id,id]}
        let json=JSON.stringify(text);
        console.log(json);
    }
}