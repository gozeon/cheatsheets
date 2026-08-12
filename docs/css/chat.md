
chat box demo  


```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <script src="//unpkg.com/alpinejs" defer></script>
  </head>
  <body>
    <div x-data="form" x-init="addMessage();addMessage();addMessage();">
      <h2><a href="https://seo-saurus.com/saurus-chronicles/reverse-scrolling-for-chat-boxes">Chat – Auto-Scroll to Latest</a></h2>
      <div
        style="
          height: 300px;
          border: 1px solid;
          overflow: auto;
          display: flex;
          flex-direction: column-reverse;
        "
      >
        <template x-if="messages">
          <template x-for="(message, index) in messages" :key="message">
            <div
              :style="{ 'justify-content': ((index % 2) === (messages.length % 2)) ? 'flex-end' : 'flex-start', 'display': 'flex', padding: '20px' }"
            >
              <div x-html="message"></div>
            </div>
          </template>
        </template>
      </div>

      <button @click="addMessage();" type="button">Add message</button>
    </div>
    <script>
      document.addEventListener('alpine:init', () => {
        Alpine.data('form', () => ({
          messages: [],
          reverse: false,
          addMessage() {
            if (this.availableMessage[this.messages.length]) {
              if (this.reverse == false) {
                this.messages = [
                  this.availableMessage[this.messages.length],
                  ...this.messages,
                ];
              } else {
                this.messages = [
                  ...this.messages,
                  this.availableMessage[this.messages.length],
                ];
              }
            }
          },
          availableMessage: [
            'Hey, how’s it going?',
            'Pretty good! How about you?',
            'Can’t complain. Did you finish that project?',
            'Yep, sent it yesterday!',
            'Awesome, I’ll check it out.',
            'What are you working on now?',
            'Just a small side project.',
            'Sounds interesting, tell me more!',
            'It’s a secret… for now. 😉',
            'Haha, okay, I’ll wait.',
            'Did you see the new update?',
            'Nope, what’s new?',
            'Better performance and new features.',
            'Nice, I’ll have to try it.',
            'Any plans for the weekend?',
            'Maybe hiking, if the weather’s nice.',
            'Good idea! Fresh air is always great.',
            'Absolutely. Clears the mind.',
            'Do you want to grab coffee tomorrow?',
            'Sure, let’s meet at 10.',
            'Perfect, see you then!',
            'Oh, and bring your laptop.',
            'Got it. Work and coffee – best combo.',
            'By the way, happy birthday!',
            'Thanks! You remembered. 🥳',
            'Of course, I brought virtual cake 🎂',
            'Yum! Even dinos love cake.',
            'Speaking of dinos, saw a funny meme today.',
            'Send it over!',
            'Incoming… prepare to laugh!',
          ],
        }));
      });
    </script>
  </body>
</html>

```
