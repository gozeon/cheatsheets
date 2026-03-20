
https://www.react-fast-marquee.com/demo

> 如果不考虑兼容问题 建议使用css animation

```ts
enum Direction {
    Left = "left",
    Right = "right",
}
interface MarqueeOption {
    direction?: Direction,
    pauseOnHover: boolean,
    speed: number,
    el: HTMLElement
}

class Marquee {
    private direction: Direction;
    private pauseOnHover: boolean = false;

    private speed: number = 10;
    private x: number = 0;
    private y: number = 0;
    private el: HTMLElement;
    private wrapper!: HTMLElement;
    private itemWidth:number = 0

    private pause = false;
    private rafId: number | null = null
    constructor(option: MarqueeOption) {

        this.direction = option?.direction ?? Direction.Left;

        this.speed = option.speed ?? 10

        this.pauseOnHover = option.pauseOnHover ?? false

        this.el = option.el

        this.init()
    }

    private init() {
// 1. Create the wrapper and move original children into it
    this.wrapper = document.createElement('div');
    this.wrapper.style.display = 'inline-flex'; // Keeps items in a row
    this.wrapper.style.whiteSpace = 'nowrap';
    
    // 2. Clone content (2 times is usually enough for the loop)
    const content = this.el.innerHTML;
    this.wrapper.innerHTML = content + content; 
    
    // 3. Clear the original container and add the wrapper
    this.el.innerHTML = '';
    this.el.style.overflow = 'hidden'; // Ensure container clips the wrapper
    this.el.appendChild(this.wrapper);

    // 4. Calculate width of ONE set of content
    // We use the first child's offsetWidth if it's a single unit, 
    // or half of the wrapper's scrollWidth since we cloned it once.
    this.itemWidth = this.wrapper.scrollWidth / 2;

    // 5. Initial position for Right direction
    if (this.direction === Direction.Right) {
        this.x = -this.itemWidth;
    }

        this.start();

        if (this.pauseOnHover) {
            this.el.addEventListener('mouseenter', () => {
                this.stop()
            })
            this.el.addEventListener('mouseleave', () => {
                this.start()
            })

        }
    }

    private loop = () => {

        switch (this.direction) {
            case Direction.Left:
                this.x -= this.speed;
                // If we've scrolled past the first element's width, jump back to 0
                if (Math.abs(this.x) >= this.itemWidth) {
                    this.x = 0;
                }
                break;

            case Direction.Right:
                this.x += this.speed;
                // If we've moved right and reached 0, jump back to the negative width
                if (this.x >= 0) {
                    this.x = -this.itemWidth;
                }
                break;
        }

        // Apply transform to all children
        for (let i = 0; i < this.el.children.length; i++) {
            const el = this.el.children[i] as HTMLElement;
            el.style.transform = `translate3d(${this.x}px, ${this.y}px, 0)`;
        }

        if (this.pause) return;
        this.rafId = requestAnimationFrame(this.loop)
    }

    public start() {
        this.pause = false
        this.loop()
    }
    public stop() {
        this.pause = true
        if (this.rafId) cancelAnimationFrame(this.rafId);
    }
}
```
