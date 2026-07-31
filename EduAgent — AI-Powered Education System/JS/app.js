const EduAgent = {
  state: JSON.parse(localStorage.getItem('eduAgentData')) || {
    trainedDocs: [], papers: [], results: [], activities: []
  },

  save() {
    localStorage.setItem('eduAgentData', JSON.stringify(this.state));
  },

  // PDF se text extract karne ka logic
  async readPDF(file) {
    const arrayBuffer = await file.arrayBuffer();
    const pdf = await pdfjsLib.getDocument({ data: arrayBuffer }).promise;
    let fullText = "";

    for (let i = 1; i <= pdf.numPages; i++) {
      const page = await pdf.getPage(i);
      const textContent = await page.getTextContent();
      fullText += textContent.items.map(item => item.str).join(" ") + "\n\n";
    }
    return fullText;
  },

  // File processing function
  async processFile(file) {
    try {
      this.addActivity(`Processing ${file.name}...`, 'blue');
      
      let content = "";
      if (file.type === "application/pdf") {
        content = await this.readPDF(file);
      } else {
        content = await file.text();
      }

      this.state.trainedDocs.push({ name: file.name, content: content });
      this.save();
      this.addActivity(`Successfully trained: ${file.name}`, 'green');
    } catch (err) {
      this.addActivity(`Error: ${err.message}`, 'red');
    }
  },

  addActivity(text, color = 'blue') {
    this.state.activities.unshift({
      text,
      color,
      time: new Date().toLocaleTimeString('en-PK', { hour: '2-digit', minute: '2-digit' })
    });
    if (this.state.activities.length > 20) this.state.activities.pop();
    this.save();
    const list = document.getElementById('activity-list');
    if (list) this.renderActivity(list);
  },

  renderActivity(el) {
    const acts = this.state.activities;
    el.innerHTML = acts.map(a => `
      <div class="activity-item">
        <div class="activity-dot ${a.color}"></div>
        <span>${a.text}</span>
        <small>${a.time}</small>
      </div>
    `).join('');
  },

  async callGroq(systemPrompt, userMessage) {
    // Groq API call logic (jo pehle thi)
    const response = await fetch('https://api.groq.com/openai/v1/chat/completions', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${window.GROQ_API_KEY}`
      },
      body: JSON.stringify({
        model: 'llama-3.3-70b-versatile',
        messages: [{ role: 'system', content: systemPrompt }, { role: 'user', content: userMessage }]
      })
    });
    const data = await response.json();
    return data.choices[0].message.content;
  }
};