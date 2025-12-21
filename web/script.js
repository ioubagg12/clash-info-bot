const form = document.getElementById("player-form");
const tagInput = document.getElementById("tag");

const resultCard = document.getElementById("result");
const errorCard = document.getElementById("error");

const playerNameEl = document.getElementById("player-name");
const playerTagEl = document.getElementById("player-tag");
const playerThEl = document.getElementById("player-th");
const playerTrophiesEl = document.getElementById("player-trophies");
const playerClanEl = document.getElementById("player-clan");

form.addEventListener("submit", (event) => {
  event.preventDefault();

  const rawTag = tagInput.value.trim();
  if (!rawTag) {
    showError("Please enter a player tag.");
    return;
  }


//demo as a placeholder for API call

  hideError();
  showResult({
    name: "Demo Player",
    tag: rawTag.toUpperCase(),
    townHallLevel: 18,
    trophies: 799,
    clan: {
      name: "Demo Clan"
    }
  });
});

function showResult(data) {
  playerNameEl.textContent = data.name;
  playerTagEl.textContent = `Tag: ${data.tag}`;
  playerThEl.textContent = `Town Hall: ${data.townHallLevel}`;
  playerTrophiesEl.textContent = `Trophies: ${data.trophies}`;
  playerClanEl.textContent = `Clan: ${data.clan?.name || "No clan"}`;

  resultCard.classList.remove("hidden");
}

function showError(message) {
  errorCard.textContent = message;
  errorCard.classList.remove("hidden");
  resultCard.classList.add("hidden");
}

function hideError() {
  errorCard.classList.add("hidden");
}
