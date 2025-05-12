let currentPage = 1;
const itemsPerPage = 30;
let products = [];

function fetchProducts() {
  fetch("http://127.0.0.1:8000/api/products")
    .then(res => res.json())
    .then(data => {
      products = data;
      renderProducts();
    });
}

function renderProducts() {
  const table = document.getElementById("productTable");
  table.innerHTML = "";
  products.forEach((product, index) => {
    const row = document.createElement("tr");
    row.innerHTML = `
      <td>${product.nome}</td>
      <td>${product.codigo}</td>
      <td>${product.entrega}</td>
      <td>${product.custo}</td>
      <td>${product.quantidade}</td>
      <td><button onclick="showProduct(${index})">ver mais</button></td>
    `;
    table.appendChild(row);
  });
}

function showProduct(index) {
  const product = products[index];
  const details = document.getElementById("productDetails");
  details.innerHTML = `
    <p><strong>Nome:</strong> ${product.nome}</p>
    <p><strong>Código:</strong> ${product.codigo}</p>
    <p><strong>Entrega:</strong> ${product.entrega}</p>
    <p><strong>Custo:</strong> ${product.custo}</p>
    <p><strong>Quantidade:</strong> ${product.quantidade}</p>
  `;

  document.getElementById("editBtn").onclick = () => editProduct(product);
  document.getElementById("deleteBtn").onclick = () => deleteProduct(product.codigo);
  openPopup("productPopup");
}

function editProduct(product) {
  const form = document.getElementById("addProductForm");
  form.nome.value = product.nome;
  form.codigo.value = product.codigo;
  form.entrega.value = product.entrega;
  form.custo.value = product.custo;
  form.quantidade.value = product.quantidade;
  openPopup("addProductPopup");

  form.onsubmit = e => {
    e.preventDefault();
    const updated = Object.fromEntries(new FormData(form));
    fetch(`http://127.0.0.1:8000/api/products/${product.codigo}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(updated)
    }).then(() => {
      closePopup("addProductPopup");
      closePopup("productPopup");
      fetchProducts();
    });
  };
}

function deleteProduct(codigo) {
  fetch(`http://127.0.0.1:8000/api/products/${codigo}`, { method: "DELETE" })
    .then(() => {
      closePopup("productPopup");
      fetchProducts();
    });
}

function openPopup(id) {
  document.getElementById(id).classList.remove("hidden");
}

function closePopup(id) {
  document.getElementById(id).classList.add("hidden");
}

document.getElementById("addProductBtn").onclick = () => {
  const form = document.getElementById("addProductForm");
  form.reset();
  form.onsubmit = e => {
    e.preventDefault();
    const product = Object.fromEntries(new FormData(form));
    fetch("http://127.0.0.1:8000/api/products", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(product)
    }).then(() => {
      closePopup("addProductPopup");
      fetchProducts();
    });
  };
  openPopup("addProductPopup");
};

document.getElementById("nextPageBtn").onclick = () => {
  currentPage++;
  fetchProducts();
};

fetchProducts();
