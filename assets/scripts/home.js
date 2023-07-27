const dir = './assets/images/home/';
const json_file = './assets/scripts/len.json'

fetch(json_file)
    .then(res => res.json())
    .then(data => {
        let len = data["length"];
        let rand = 1;
        let check = [0, 0, 0];

        for (let i = 0; i < 4; i++) {
            rand = Math.random();
            rand = Math.floor(rand * (len + 1));
            let image = rand;
            if (!check.includes(rand)) {
                check[i] = rand;
                var image_node = new Image();
                image_node.alt = "pic";
                image_node.loading = "lazy";
                image_node.src = dir + rand + ".jpg";
                image_node.style =
                "min-width:320px; display: flex; flex-wrap:wrap; justify-content: space-between; margin-top:20px";
                document.getElementById("images").appendChild(image_node);
            } else {
                i -= 1;
            }
        }
    });