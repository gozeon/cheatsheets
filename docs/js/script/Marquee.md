
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

export class Marquee {
    private direction: Direction;
    private pauseOnHover: boolean = false;

    private speed: number = 0;
    private x: number = 0;
    private y: number = 0;
    private el: HTMLElement;
    private wrapper!: HTMLElement;
    private itemWidth: number = 0

    private pause = false;
    private rafId: number | null = null
    constructor(option: MarqueeOption) {

        this.direction = option?.direction ?? Direction.Left;

        this.speed = option.speed ?? 2

        this.pauseOnHover = option.pauseOnHover ?? false

        this.el = option.el

        this.init()
    }

    private init() {
        // 1. 此时 el 里面还是你原始的 HTML
        // 设置 whiteSpace 确保内容不换行，否则 scrollWidth 测量不准
        this.el.style.whiteSpace = 'nowrap';
        this.el.style.display = 'block';

        // 2. 直接获取原始内容的真实滚动宽度
        this.itemWidth = this.el.scrollWidth;

        // 3. 现在再进行克隆和包裹逻辑
        const content = this.el.innerHTML;

        this.wrapper = document.createElement('div');
        this.wrapper.style.display = 'inline-flex';
        this.wrapper.innerHTML = content + content + content; // 克隆

        this.el.innerHTML = '';
        this.el.appendChild(this.wrapper);

        // 4. 设置初始位置
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
