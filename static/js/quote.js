const quotes = [
  "TRY NOT TO BECOME A MAN OF SUCCESS, BUT RATHER TRY TO BECOME A MAN OF VALUE.\n" +
    " - Albert Einstein",

  "DO NOT GO WHERE THE PATH MAY LEAD, GO INSTEAD WHERE THERE IS NO PATH AND LEAVE A TRAIL.\n" +
    " - Ralph Waldo",

  "YOU MUST BE THE CHANGE YOU WISH TO SEE IN THE WORLD.\n" +
    " - Mahatma Gandhi",

  "THE OLDEST, SHORTEST WORDS 'YES' AND 'NO' - ARE THOSE WHICH REQUIRE THE MOST THOUGHT.\n" +
    " - Pythagoras",

  "IMAGINATION IS MORE IMPORTANT THAN KNOWLEDGE.\n" + " - Albert Einstein",

  "ALL OUR DREAMS CAN COME TRUE, IF WE HAVE THE COURAGE TO PURSUE THEM.\n" +
    " - Walt Disney",
];

// Function to get daily quote
function getDailyQuote() {
  // Use the current date to generate a consistent index
  const today = new Date();
  const index = today.getDate() % quotes.length; // Rotate through the quotes

  // Return the selected quote
  return quotes[index];
}

// Display the daily quote
const quoteElement = document.getElementById("daily-quote");
if (quoteElement) {
  quoteElement.innerText = getDailyQuote();
} else {
  console.log(getDailyQuote()); // Fallback if an element doesn't exist
}
