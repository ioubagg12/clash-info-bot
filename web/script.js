// --- Player Info Section ---
const playerForm = document.getElementById("player-form");
const playerTagInput = document.getElementById("player-tag-input");
const playerResultCard = document.getElementById("player-result");
const playerErrorCard = document.getElementById("player-error");

const playerNameEl = document.getElementById("player-name");
const playerTagEl = document.getElementById("player-tag");
const playerThEl = document.getElementById("player-th");
const playerTrophiesEl = document.getElementById("player-trophies");
const playerClanEl = document.getElementById("player-clan");

playerForm.addEventListener("submit", (event) => {
  event.preventDefault();

  const rawTag = playerTagInput.value.trim();
  if (!rawTag) {
    showPlayerError("Please enter a player tag.");
    return;
  }

  // Demo data for Player
  hidePlayerError();
  showPlayerResult({
    name: "Demo Player",
    tag: rawTag.toUpperCase(),
    townHallLevel: 13,
    trophies: 5200,
    clan: {
      name: "Demo Clan"
    }
  });
});

function showPlayerResult(data) {
  playerNameEl.textContent = data.name;
  playerTagEl.textContent = `Tag: ${data.tag}`;
  playerThEl.textContent = `Town Hall: ${data.townHallLevel}`;
  playerTrophiesEl.textContent = `Trophies: ${data.trophies}`;
  playerClanEl.textContent = `Clan: ${data.clan?.name || "No clan"}`;

  playerResultCard.classList.remove("hidden");
}

function showPlayerError(message) {
  playerErrorCard.textContent = message;
  playerErrorCard.classList.remove("hidden");
  playerResultCard.classList.add("hidden");
}

function hidePlayerError() {
  playerErrorCard.classList.add("hidden");
}


// --- Clan Info Section ---
const clanForm = document.getElementById("clan-form");
const clanTagInput = document.getElementById("clan-tag-input");
const clanResultCard = document.getElementById("clan-result");
const clanErrorCard = document.getElementById("clan-error");

const clanNameEl = document.getElementById("clan-name");
const clanTagEl = document.getElementById("clan-tag");
const clanLevelEl = document.getElementById("clan-level");
const clanPointsEl = document.getElementById("clan-points");
const clanMembersEl = document.getElementById("clan-members");

clanForm.addEventListener("submit", (event) => {
  event.preventDefault();

  const rawTag = clanTagInput.value.trim();
  if (!rawTag) {
    showClanError("Please enter a clan tag.");
    return;
  }

  // Demo data for Clan
  hideClanError();
  showClanResult({
    name: "Demo Clan",
    tag: rawTag.toUpperCase(),
    clanLevel: 15,
    clanPoints: 45000,
    members: 48
  });
});

function showClanResult(data) {
  clanNameEl.textContent = data.name;
  clanTagEl.textContent = `Tag: ${data.tag}`;
  clanLevelEl.textContent = `Level: ${data.clanLevel}`;
  clanPointsEl.textContent = `Points: ${data.clanPoints}`;
  clanMembersEl.textContent = `Members: ${data.members}/50`;

  clanResultCard.classList.remove("hidden");
}

function showClanError(message) {
  clanErrorCard.textContent = message;
  clanErrorCard.classList.remove("hidden");
  clanResultCard.classList.add("hidden");
}

function hideClanError() {
  clanErrorCard.classList.add("hidden");
}
