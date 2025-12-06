// Inicializar cuando el DOM esté listo
document.addEventListener('DOMContentLoaded', function() {
    initHamburgerMenu();
    initFileUpload();
    initFormValidation();
    initDetailsAnimation();
    initScrollToTop();
});

/* ============ HAMBURGER MENU ============ */

function initHamburgerMenu() {
    const hamburger = document.getElementById('hamburger');
    const navbarMenu = document.getElementById('navbarMenu');

    if (hamburger && navbarMenu) {
        hamburger.addEventListener('click', function() {
            navbarMenu.classList.toggle('active');
            hamburger.classList.toggle('active');
        });

        // Cerrar el menú cuando se hace clic en un enlace
        const navLinks = navbarMenu.querySelectorAll('a');
        navLinks.forEach(link => {
            link.addEventListener('click', function() {
                navbarMenu.classList.remove('active');
                hamburger.classList.remove('active');
            });
        });

        // Cerrar el menú cuando se hace clic fuera de él
        document.addEventListener('click', function(event) {
            if (!event.target.closest('.navbar')) {
                navbarMenu.classList.remove('active');
                hamburger.classList.remove('active');
            }
        });
    }
}

/* ============ FILE UPLOAD ============ */

function initFileUpload() {
    const fileUploadAreas = document.querySelectorAll('.file-upload-area');

    fileUploadAreas.forEach(area => {
        const fileInput = area.parentElement.querySelector('.file-input');
        
        if (fileInput) {
            // Click para abrir el input
            area.addEventListener('click', function() {
                fileInput.click();
            });

            // Drag and drop
            area.addEventListener('dragover', function(e) {
                e.preventDefault();
                area.style.borderColor = '#2563eb';
                area.style.backgroundColor = '#f0f9ff';
            });

            area.addEventListener('dragleave', function() {
                area.style.borderColor = '#e5e7eb';
                area.style.backgroundColor = '#f9fafb';
            });

            area.addEventListener('drop', function(e) {
                e.preventDefault();
                area.style.borderColor = '#e5e7eb';
                area.style.backgroundColor = '#f9fafb';
                
                const files = e.dataTransfer.files;
                if (files.length > 0) {
                    fileInput.files = files;
                    updateFileInputLabel(fileInput, area);
                }
            });

            // Cambio en el input
            fileInput.addEventListener('change', function() {
                updateFileInputLabel(this, area);
            });
        }
    });
}

function updateFileInputLabel(input, area) {
    if (input.files.length > 0) {
        const fileName = input.files[0].name;
        const fileSize = (input.files[0].size / 1024 / 1024).toFixed(2);
        
        const label = area.querySelector('h4');
        if (label) {
            label.textContent = `✓ Archivo seleccionado: ${fileName}`;
            label.style.color = '#10b981';
        }

        const desc = area.querySelector('p');
        if (desc) {
            desc.textContent = `${fileSize} MB`;
        }
    }
}

/* ============ FORM VALIDATION ============ */

function initFormValidation() {
    const forms = document.querySelectorAll('form');
    
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const requiredFields = form.querySelectorAll('[required]');
            let isValid = true;

            requiredFields.forEach(field => {
                if (!field.value.trim()) {
                    isValid = false;
                    field.style.borderColor = '#ef4444';
                    showErrorMessage(field, 'Este campo es requerido');
                } else {
                    field.style.borderColor = '#e5e7eb';
                    clearErrorMessage(field);
                }
            });

            if (!isValid) {
                e.preventDefault();
            }
        });

        // Limpiar error cuando el usuario escribe
        const inputs = form.querySelectorAll('input, textarea, select');
        inputs.forEach(input => {
            input.addEventListener('change', function() {
                if (this.value.trim()) {
                    this.style.borderColor = '#e5e7eb';
                    clearErrorMessage(this);
                }
            });
        });
    });
}

function showErrorMessage(field, message) {
    const errorDiv = document.createElement('div');
    errorDiv.className = 'form-error';
    errorDiv.textContent = message;
    errorDiv.style.color = '#ef4444';
    errorDiv.style.fontSize = '0.85rem';
    errorDiv.style.marginTop = '0.5rem';
    
    const existing = field.parentElement.querySelector('.form-error');
    if (existing) existing.remove();
    field.parentElement.appendChild(errorDiv);
}

function clearErrorMessage(field) {
    const errorDiv = field.parentElement.querySelector('.form-error');
    if (errorDiv) errorDiv.remove();
}

/* ============ DETAILS ANIMATION ============ */

function initDetailsAnimation() {
    const detailsElements = document.querySelectorAll('details');

    detailsElements.forEach(details => {
        const summary = details.querySelector('summary');
        const content = details.querySelector('details > *:not(summary)');

        if (summary && content) {
            // Animar la apertura
            details.addEventListener('toggle', function() {
                if (this.open) {
                    content.style.display = 'block';
                    summary.style.backgroundColor = '#f0f9ff';
                } else {
                    summary.style.backgroundColor = '#f9fafb';
                }
            });
        }
    });
}

/* ============ SCROLL TO TOP ============ */

function initScrollToTop() {
    // Crear botón
    const scrollToTopBtn = document.createElement('button');
    scrollToTopBtn.id = 'scrollToTopBtn';
    scrollToTopBtn.innerHTML = '<i class="fas fa-arrow-up"></i>';
    scrollToTopBtn.title = 'Volver al inicio';
    
    const style = document.createElement('style');
    style.textContent = `
        #scrollToTopBtn {
            position: fixed;
            bottom: 2rem;
            right: 2rem;
            background-color: #2563eb;
            color: white;
            border: none;
            border-radius: 50%;
            width: 50px;
            height: 50px;
            font-size: 1.2rem;
            cursor: pointer;
            display: none;
            align-items: center;
            justify-content: center;
            z-index: 999;
            box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3);
            transition: all 0.3s ease;
        }

        #scrollToTopBtn:hover {
            background-color: #1e40af;
            transform: translateY(-3px);
        }

        #scrollToTopBtn.show {
            display: flex;
        }

        @media (max-width: 768px) {
            #scrollToTopBtn {
                bottom: 1rem;
                right: 1rem;
                width: 45px;
                height: 45px;
            }
        }
    `;
    
    document.head.appendChild(style);
    document.body.appendChild(scrollToTopBtn);

    // Mostrar/ocultar según scroll
    window.addEventListener('scroll', function() {
        if (window.pageYOffset > 300) {
            scrollToTopBtn.classList.add('show');
        } else {
            scrollToTopBtn.classList.remove('show');
        }
    });

    // Scroll al hacer clic
    scrollToTopBtn.addEventListener('click', function() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
}

/* ============ UTILITIES ============ */

// Mostrar notificaciones
function showNotification(message, type = 'info') {
    const alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${type} alert-dismissible`;
    alertDiv.innerHTML = `
        <button type="button" class="alert-close" onclick="this.parentElement.style.display='none';">
            <i class="fas fa-times"></i>
        </button>
        <i class="fas fa-info-circle"></i>
        ${message}
    `;

    const container = document.querySelector('.alerts-container') || document.querySelector('.main-content');
    if (container) {
        container.insertBefore(alertDiv, container.firstChild);
        
        // Auto-cerrar después de 5 segundos
        setTimeout(() => {
            alertDiv.style.display = 'none';
        }, 5000);
    }
}

// Formatear fecha
function formatDate(dateString) {
    const date = new Date(dateString);
    const options = { year: 'numeric', month: 'long', day: 'numeric', hour: '2-digit', minute: '2-digit' };
    return date.toLocaleDateString('es-CO', options);
}

// Validar email
function validateEmail(email) {
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regex.test(email);
}

// Copiar al portapapeles
function copyToClipboard(text) {
    navigator.clipboard.writeText(text).then(() => {
        showNotification('Copiado al portapapeles', 'success');
    }).catch(() => {
        showNotification('Error al copiar', 'error');
    });
}

// Confirmar acción
function confirmAction(message) {
    return confirm(message);
}

/* ============ FILTROS DINÁMICOS ============ */

function setupFilterButtons() {
    const filterBtns = document.querySelectorAll('.filter-btn');
    const cards = document.querySelectorAll('[data-status]');

    filterBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            const filter = this.dataset.filter;

            // Actualizar botones activos
            filterBtns.forEach(b => b.classList.remove('active'));
            this.classList.add('active');

            // Filtrar tarjetas
            cards.forEach(card => {
                if (filter === 'all' || card.dataset.status === filter) {
                    card.style.display = 'block';
                    setTimeout(() => {
                        card.style.opacity = '1';
                        card.style.transform = 'translateY(0)';
                    }, 10);
                } else {
                    card.style.opacity = '0';
                    card.style.transform = 'translateY(10px)';
                    setTimeout(() => {
                        card.style.display = 'none';
                    }, 300);
                }
            });
        });
    });
}

// Inicializar filtros si existen
if (document.querySelector('.filter-btn')) {
    setTimeout(setupFilterButtons, 100);
}

/* ============ TOOLTIPS ============ */

function initTooltips() {
    const tooltipElements = document.querySelectorAll('[title]');

    tooltipElements.forEach(element => {
        element.addEventListener('mouseenter', function() {
            const tooltip = document.createElement('div');
            tooltip.className = 'tooltip';
            tooltip.textContent = this.title;
            tooltip.style.position = 'absolute';
            tooltip.style.backgroundColor = '#1f2937';
            tooltip.style.color = 'white';
            tooltip.style.padding = '0.5rem 1rem';
            tooltip.style.borderRadius = '0.25rem';
            tooltip.style.fontSize = '0.85rem';
            tooltip.style.zIndex = '1000';
            tooltip.style.whiteSpace = 'nowrap';
            tooltip.style.pointerEvents = 'none';
            
            document.body.appendChild(tooltip);
            
            const rect = this.getBoundingClientRect();
            tooltip.style.top = (rect.top - tooltip.offsetHeight - 10) + 'px';
            tooltip.style.left = (rect.left + (rect.width - tooltip.offsetWidth) / 2) + 'px';
        });

        element.addEventListener('mouseleave', function() {
            const tooltips = document.querySelectorAll('.tooltip');
            tooltips.forEach(t => t.remove());
        });
    });
}

// Inicializar tooltips
setTimeout(initTooltips, 100);

/* ============ CONSOLE MESSAGES ============ */

console.log('%c🎓 EduLearn - Plataforma de Educación Online', 'font-size: 16px; font-weight: bold; color: #2563eb;');
console.log('%cBienvenido a nuestra plataforma de aprendizaje', 'font-size: 12px; color: #6b7280;');