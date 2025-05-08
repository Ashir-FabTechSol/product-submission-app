document.addEventListener('DOMContentLoaded', () => {
    loadProducts();

    const productForm = document.getElementById('productForm');
    const nameField = document.getElementById('name');
    const priceField = document.getElementById('price');
    const descriptionField = document.getElementById('description');

    productForm.addEventListener('submit', async (e) => {
        e.preventDefault();

        clearErrors();

        const name = nameField.value.trim();
        const price = priceField.value.trim();
        const description = descriptionField.value.trim();

        let hasError = false;

        if (!name) {
            showError('name', 'Product name is required');
            hasError = true;
        }

        const priceValue = parseFloat(price);
        if (!price || isNaN(priceValue) || priceValue <= 0) {
            showError('price', 'Please enter a valid price greater than 0');
            hasError = true;
        }

        if (hasError) {
            const firstErrorInput = document.querySelector('.error');
            if (firstErrorInput) firstErrorInput.focus();
            return;
        }

        const formData = {
            name: name,
            price: priceValue,
            description: description
        };

        try {
            // Disable button to prevent multiple submissions
            const submitButton = productForm.querySelector('button[type="submit"]');
            submitButton.disabled = true;
            submitButton.textContent = 'Submitting...';

            const response = await fetch('/api/products', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(formData)
            });

            submitButton.disabled = false;
            submitButton.textContent = 'Add Product';

            if (response.ok) {
                showSuccess('Product added successfully!');
                productForm.reset();
                loadProducts();
            } else {
                const error = await response.json();
                showError('form', error.error || 'Error adding product');
            }
        } catch (error) {
            console.error('Error:', error);
            showError('form', 'Server error while adding product');
        }
    });

    function showError(field, message) {
        const errorDiv = document.createElement('div');
        errorDiv.className = 'error-message show';
        errorDiv.textContent = message;

        if (field === 'form') {
            productForm.insertBefore(errorDiv, productForm.firstChild);
        } else {
            const inputField = document.getElementById(field);
            inputField.classList.add('error');
            inputField.parentNode.appendChild(errorDiv);
        }
    }

    function showSuccess(message) {
        const successDiv = document.createElement('div');
        successDiv.className = 'success-message show';
        successDiv.textContent = message;
        productForm.insertBefore(successDiv, productForm.firstChild);
        setTimeout(() => successDiv.remove(), 3000);
    }

    function clearErrors() {
        document.querySelectorAll('.error-message').forEach(error => error.remove());
        document.querySelectorAll('.error').forEach(field => field.classList.remove('error'));
    }

    function formatLocalTime(isoString) {
        const date = new Date(isoString);
        return date.toLocaleString(undefined, {
            year: 'numeric',
            month: 'short',
            day: 'numeric',
            hour: '2-digit',
            minute: '2-digit',
            second: '2-digit',
            hour12: true,
            timeZoneName: 'short'
        });
    }

    async function loadProducts() {
        try {
            const response = await fetch('/api/products');
            const products = await response.json();

            const productList = document.getElementById('productList');
            productList.innerHTML = products.map(product => `
                <div class="product-item">
                    <div class="product-name">Product Name: ${product.name}</div>
                    <div class="product-price">Product Price: $${product.price.toFixed(2)}</div>
                    ${product.description ? `<div class="product-description">Product Description: ${product.description}</div>` : ''}
                    <div class="product-date"><i class="fas fa-clock"></i> ${formatLocalTime(product.created_at)}</div>
                </div>
            `).join('');
        } catch (error) {
            console.error('Error:', error);
            productList.innerHTML = '<p class="error-message show">Error loading products</p>';
        }
    }
});

