window.addEventListener('load', ()=>{
    const canvas = document.querySelector('#canvas');
    const ctx = canvas.getContext('2d');

    //resizing
    canvas.height = 500;
    canvas.width = 500;

    //variables
    let painting = false;

    function startPosition(e){
        painting = true;
        draw(e);
    }

    function finishPosition(){
        painting = false;
        ctx.beginPath();
        console.log("predict")
    }

    function draw(e){
        if(!painting) return;
        ctx.lineWidth = 10;
        ctx.lineCap = 'round';
        ctx.lineTo(e.clientX-100, e.clientY-100);
        ctx.stroke();
        ctx.beginPath();
        ctx.moveTo(e.clientX-100, e.clientY-100);
    }

    //eventlisteners
    canvas.addEventListener('mousedown', startPosition);
    canvas.addEventListener('mouseup', finishPosition);
    canvas.addEventListener('mousemove', draw);

    btn = document.querySelector('#predict_me');
    clr_btn  =document.querySelector('#clear');

    clr_btn.addEventListener('click', function(){
        console.log("Canvs ccleared");
        ctx.clearRect(0, 0, 500, 500);
    })

    btn.addEventListener('click', function(){
        const canvas = document.querySelector('#canvas');
        const dataURI = canvas.toDataURL();
        console.log(dataURI);


        // if(window.navigator.msSaveBlob){
        //     window.navigator.msSaveBlob(canvas.msToBlob(), 'canvas-image.png');
        // }else{
        //     const a = document.createElement('a');

        //     document.body.appendChild(a);
        //     a.href = canvas.toDataURL();
        //     a.download = 'D:/Projects/DawringToDrawing/DawringDrawing/images/canvas-image.png';
        //     a.click();
        //     document.body.removeChild(a);

    // });
})})