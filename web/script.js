//  demo data for Player
const playerForm = document.getElementById("player-form");
const playerTagInput = document.getElementById("player-tag-input");
const playerResultCard = document.getElementById("player-result");
const playerErrorCard = document.getElementById("player-error");

const playerNameEl = document.getElementById("player-name");
const playerTagEl = document.getElementById("player-tag");
const playerThEl = document.getElementById("player-th");
const playerTrophiesEl = document.getElementById("player-trophies");
const playerClanEl = document.getElementById("player-clan");

playerForm.addEventListener("submit", async (event) => {
  event.preventDefault();

  const rawTag = playerTagInput.value.trim();
  if (!rawTag) {
    showPlayerError("Please enter a player tag.");
    return;
  }

  hidePlayerError();
  playerResultCard.classList.add("hidden");

  // Show a temporary loading message
  playerNameEl.textContent = "Loading...";
  playerTagEl.textContent = "";
  playerThEl.textContent = "";
  playerTrophiesEl.textContent = "";
  playerClanEl.textContent = "";
  playerResultCard.classList.remove("hidden");

  try {
    const url = "http://127.0.0.1:8000/player?tag=" + encodeURIComponent(rawTag);

    const response = await fetch(url);
    const data = await response.json();

    if (!response.ok || !data.success) {
      showPlayerError(data.error || "Failed to fetch player info.");
      return;
    }

    const p = data.player;

    playerNameEl.textContent = p.name || "Unknown";
    playerTagEl.textContent = "Tag: " + (p.tag || rawTag.toUpperCase());
    playerThEl.textContent = "Town Hall: " + (p.townHallLevel ?? "N/A");
    playerTrophiesEl.textContent = "Trophies: " + (p.trophies ?? "N/A");

    if (p.clan && p.clan.name) {
      playerClanEl.textContent =
        "Clan: " +
        p.clan.name +
        (p.clan.level ? " (Level " + p.clan.level + ")" : "");
    } else {
      playerClanEl.textContent = "Clan: No clan";
    }

    playerResultCard.classList.remove("hidden");
  } catch (err) {
    console.error(err);
    showPlayerError("Error talking to the server. Is it running?");
  }
});

function showPlayerError(message) {
  playerErrorCard.textContent = message;
  playerErrorCard.classList.remove("hidden");
  playerResultCard.classList.add("hidden");
}

function hidePlayerError() {
  playerErrorCard.classList.add("hidden");
}


//  demo data for Clan
const clanForm = document.getElementById("clan-form");
const clanTagInput = document.getElementById("clan-tag-input");
const clanResultCard = document.getElementById("clan-result");
const clanErrorCard = document.getElementById("clan-error");

const clanNameEl = document.getElementById("clan-name");
const clanTagEl = document.getElementById("clan-tag");
const clanLevelEl = document.getElementById("clan-level");
const clanPointsEl = document.getElementById("clan-points");
const clanMembersEl = document.getElementById("clan-members");

clanForm.addEventListener("submit", async (event) => {
  event.preventDefault();

  const rawTag = clanTagInput.value.trim();
  if (!rawTag) {
    showClanError("Please enter a clan tag.");
    return;
  }

  hideClanError();
  clanResultCard.classList.add("hidden");

  // Show loading state
  clanNameEl.textContent = "Loading...";
  clanTagEl.textContent = "";
  clanLevelEl.textContent = "";
  clanPointsEl.textContent = "";
  clanMembersEl.textContent = "";
  clanResultCard.classList.remove("hidden");

  try {
    const url = "http://127.0.0.1:8000/clan?tag=" + encodeURIComponent(rawTag);

    const response = await fetch(url);
    const data = await response.json();

    if (!response.ok || !data.success) {
      showClanError(data.error || "Failed to fetch clan info.");
      return;
    }

    showClanResult(data.clan);

  } catch (err) {
    console.error(err);
    showClanError("Error talking to the server. Is it running?");
  }
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
