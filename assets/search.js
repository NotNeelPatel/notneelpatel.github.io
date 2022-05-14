const dataTemplate = document.querySelector("[data-template]")
const entryContainer = document.querySelector("[data-entries-container")
const searchInput = document.querySelector("[data-search]")

let entries = []

searchInput.addEventListener("input", e => {
    const value = e.target.value.toLowerCase()
    entries.forEach(entry => {
        const isVisible = entry.title.toLowerCase().includes(value) || entry.url.toLowerCase().includes(value)
        entry.element.classList.toggle("hide", !isVisible)
    })

})

fetch('./assets/searchindex.json')
    .then(res => res.json())
    .then(data => {
        entries = data.map(entry => {
            const card = dataTemplate.content.cloneNode(true).children[0]
            const links = card.querySelector("[data-links]")
            links.textContent = entry.title
            links.href = entry.url
            entryContainer.append(card)
            return { title: entry.title, url: entry.url, element: card }

        })

    })

