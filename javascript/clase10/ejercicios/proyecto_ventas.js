class Producto {
  static contadorProductos = 0;

  constructor(nombre, precio) {
    this.idProducto = ++Producto.contadorProductos;
    this._nombre = nombre;
    this._precio = precio;
  }

  get IdProducto() {
    return this.idProducto;
  }

  get Nombre() {
    return this._nombre;
  }
  set Nombre(nombre) {
    this._nombre = nombre;
  }

  get Precio() {
    return this._precio;
  }

  set Precio(precio) {
    const n = Number(precio);
    if (!Number.isFinite(n) || n < 0) {
      throw new TypeError("El precio debe ser un número >= 0");
    }
    this._precio = n;
  }

  // usando template literals
  toString() {
    return `Producto #${this.IdProducto} - ${
      this.Nombre
    } ($${this.Precio.toFixed(2)})`;
  }
}

class Orden {
  static contadorOrdenes = 0;
  static MAX_PRODUCTOS = 5;

  constructor() {
    this._idOrden = ++Orden.contadorOrdenes;
    this._productos = [];
    this._contadorProductosAgregados = 0;
  }

  agregarProducto(producto) {
    if (!(producto instanceof Producto)) {
      throw new TypeError("Solo pueden agregarse instancias de Producto");
    }
    if (this._productos.length >= Orden.MAX_PRODUCTOS) {
      return false; // máximo alcanzado
    }
    this._productos.push(producto);
    this.contadorProductosAgregados++;
    return true;
  }

  calcularTotal() {
    return this._productos.reduce((acc, p) => acc + p.Precio, 0);
  }

  mostrarOrden() {
    console.log("Orden N° " + this._idOrden);

    if (this._productos.length === 0) {
      console.log("No hay productos en esta orden.");
      return;
    }

    console.log("Productos:");
    for (let i = 0; i < this._productos.length; i++) {
      const producto = this._productos[i];
      console.log(i + 1 + ". " + producto.Nombre + " - $" + producto.Precio);
    }

    console.log("Total: $" + this.calcularTotal());
  }
}

const p1 = new Producto("Mouse", 12.5);
const p2 = new Producto("Teclado", 35);
const p3 = new Producto("Monitor", 199.999);
const p4 = new Producto("Laptop", 1500);
const p5 = new Producto("Parlantes", 250);
const p6 = new Producto("Camara", 80);
p4._precio = 1400;

const orden1 = new Orden();
orden1.agregarProducto(p1);
orden1.agregarProducto(p2);
orden1.agregarProducto(p3);
orden1.mostrarOrden();

const orden2 = new Orden();
orden2.agregarProducto(p4);
orden2.agregarProducto(p5);
orden2.agregarProducto(p2);
orden2.agregarProducto(p1);
orden2.agregarProducto(p3);
orden2.agregarProducto(p6); // no se agrega (máximo 5)
// orden2.mostrarOrden()
