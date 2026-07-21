const canva = document.getElementById('canva')
const ctx = canva.getContext('2d')
canva.width = document.getElementById('accueil').offsetWidth
canva.height =  document.getElementById('accueil').offsetHeight
let node_count = 15 
if (window.innerWidth <= 768) {
    node_count = 8
}
let nodes = new Array(node_count)
for (let i=0;i<node_count;i++){
    let x_max= canva.width
    let y_max = canva.height
    let v_min = -2
    let v_max = 2
    let x = Math.floor(Math.random()*(x_max + 1));
    let y = Math.floor(Math.random()*(y_max + 1));
    let vx = Math.random()*(v_max - v_min + 1) -2;
    let vy = Math.random()*(v_max - v_min + 1) -2;
    nodes[i] = {x:x,y:y,vx:vx,vy:vy}
    console.log(nodes[i])
}
const reducedMotion = matchMedia('(prefers-reduced-motion: reduce)').matches
function draw() {
    ctx.clearRect(0,0,canva.width,canva.height)
    for (let i=0;i<nodes.length;i++) {
        if (nodes[i].x>=canva.width || nodes[i].x<=0) {
        nodes[i].vx *= -1
        }
        if (nodes[i].y>=canva.height || nodes[i].y<=0) {
            nodes[i].vy *= -1
        }
        nodes[i].x += nodes[i].vx
        nodes[i].y += nodes[i].vy
    }
    for (let i=0;i<nodes.length;i++){
        for(let j= i+1;j<nodes.length;j++){
            var dx = (nodes[j].x - nodes[i].x)
            var dy = (nodes[j].y - nodes[i].y)
            var distance = Math.sqrt(dx*dx + dy*dy)
            const distance_max = 150
            var ratio_brut = distance / distance_max
            var ratio = 1 - ratio_brut
            if (distance< distance_max){
                ctx.beginPath()
                ctx.moveTo(nodes[i].x,nodes[i].y)
                ctx.lineTo(nodes[j].x,nodes[j].y)
                ctx.strokeStyle = `rgba(0,229,160,${ratio})`
                ctx.stroke();
            }
        }
    }
    for (let i=0;i<nodes.length;i++) {
        ctx.beginPath();
        ctx.arc(nodes[i].x,nodes[i].y,5,0,Math.PI*2);
        ctx.fillStyle = '#00E5A0';
        ctx.fill();
    }
    if (reducedMotion == false) {
        requestAnimationFrame(draw)
    }
}
draw()
let timer;
function resize(){
    window.addEventListener('resize',function(){
    clearTimeout(timer)
    timer = setTimeout(function(){
    canva.width = document.getElementById('accueil').offsetWidth
    canva.height = document.getElementById('accueil').offsetHeight
    for (let i=0;i<nodes.length;i++){
            nodes[i].x = Math.max(Math.min(nodes[i].x,canva.width),0)
            nodes[i].y = Math.max(Math.min(nodes[i].y,canva.height),0)
    }
    },200)
    })
}
resize()