

https://css-tricks.com/lets-create-a-lightweight-native-event-bus-in-javascript/

## eventbus

```js title="Eventbus.js"
class EventBus {
    constructor(description = '') {
        this.eventTarget = document.appendChild(document.createComment(description));
    }
    on(type, listener) {
        this.eventTarget.addEventListener(type, listener);
    }
    once(type, listener) {
        this.eventTarget.addEventListener(type, listener, { once: true });
    }
    off(type, listener) {
        this.eventTarget.removeEventListener(type, listener);
    }
    emit(type, detail) {
        return this.eventTarget.dispatchEvent(new CustomEvent(type, { detail }));
    }
}

// option
export default new EventBus('eventbus');

```
