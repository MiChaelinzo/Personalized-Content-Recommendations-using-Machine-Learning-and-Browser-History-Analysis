// Get the user's browsing history
chrome.history.search({text: '', startTime: 0, maxResults: 1000}, function(historyItems) {
    // Loop through the history items and extract the URLs
    var urls = [];
    for (var i = 0; i < historyItems.length; i++) {
        urls.push(historyItems[i].url);
    }
    
    // Pass the URLs to the preprocessing function
    var preprocessed_history = preprocess_history(urls);
});
