const planetArray = [
    { planet: 'Mercury', moon: 0 },
    { planet: 'Venus', moon: 0 },
    { planet: 'Earth', moon: 1 },
    { planet: 'Mars', moon: 2 },
    { planet: 'Jupiter', moon: 0 },
    { planet: 'Saturn', moon: 82 },
    { planet: 'Jupiter', moon: 79 },
    { planet: 'Uranus', moon: 27 },
    { planet: 'Neptune', moon: 14 }
];

const section = document.querySelector('section');
// let planetArray=[ "Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
for (let planets of planetArray) {

    const divelement = document.createElement("div")
    // document.body.append(divelement)
    divelement.classList.add('planet')
    divelement.classList.add(planets.planet)

    for (let i = 0; i < planets.moon; i++) {
        const moonDiv = document.createElement("div")
        moonDiv.classList.add('moon')
        moonDiv.style.left=i*12+'px'
        divelement.appendChild(moonDiv)
    }
    const section = document.querySelector(".listPlanets");
    section.appendChild(divelement)
}



