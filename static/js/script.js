
// Setup Three.js scene
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth/window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer({ antialias: true });
renderer.setSize(window.innerWidth, window.innerHeight);
document.getElementById("viz").appendChild(renderer.domElement);

// Earth sphere
const earthTexture = new THREE.TextureLoader().load('/static/textures/earth_daymap.jpg');
const geometry = new THREE.SphereGeometry(4, 64, 64);
const material = new THREE.MeshPhongMaterial({ map: earthTexture });
const earth = new THREE.Mesh(geometry, material);
scene.add(earth);

// Lights
const light = new THREE.PointLight(0xffffff, 1);
light.position.set(10, 10, 10);
scene.add(light);

camera.position.z = 15;



function animate() {
    requestAnimationFrame(animate);
    earth.rotation.y += 0.0005; // slow rotation
    renderer.render(scene, camera);
}
animate();