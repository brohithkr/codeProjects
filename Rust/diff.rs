fn diff(f: fn(f64) -> f64, x: f64, h: f64) -> f64 {
    (f(x+h)-f(x-h))/(2.0*h)
}

fn main() {
    let val = diff(|x| 3.0*x*x*x + 2.0*x*x, 1.0, 1e-6);
    println!("{}", val);
}