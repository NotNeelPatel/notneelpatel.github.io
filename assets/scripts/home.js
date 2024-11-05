const dir = './assets/images/home/';
const LENGTH = 71;

let len = LENGTH;
let rand = 1;
let check = [0, 0, 0, 0];

for (let i = 0; i < 4; i++) {
    rand = Math.random();
    rand = Math.floor(1 + rand * len);
    let image = rand;
    if (!check.includes(rand)) {
        check[i] = rand;
        var image_node = new Image();
        image_node.alt = "pic";
        image_node.loading = "lazy";
        image_node.src = dir + rand + ".jpg";
        image_node.style =
        "display: flex; flex-wrap:wrap; justify-content: space-between; margin-top:20px";
        document.getElementById("images").appendChild(image_node);
    } else {
        i -= 1;
    }
}
