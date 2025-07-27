const fileInput = document.getElementById('fileInput');
const uploadBox = document.getElementById('uploadBox');
const uploadText = document.getElementById('uploadText');
const uploadTitle = document.getElementById('uploadTitle');
const previewImage = document.getElementById('previewImage');
const fileInfo = document.getElementById('fileInfo');
const fileName = document.getElementById('fileName');
const fileSize = document.getElementById('fileSize');
const errorMessage = document.getElementById('errorMessage');
const submitBtn = document.getElementById('submitBtn');
const submitText = document.getElementById('submitText');
const loadingSpinner = document.getElementById('loadingSpinner');
const resetBtn = document.getElementById('resetBtn');
const uploadForm = document.getElementById('uploadForm');

// Constantes
const MAX_FILE_SIZE = 10 * 1024 * 1024; // 10MB
const ACCEPTED_TYPES = ['image/jpeg', 'image/jpg', 'image/png', 'image/gif'];

// Event listeners
uploadBox.addEventListener('click', () => fileInput.click());
uploadBox.addEventListener('dragover', handleDragOver);
uploadBox.addEventListener('dragleave', handleDragLeave);
uploadBox.addEventListener('drop', handleDrop);
fileInput.addEventListener('change', handleFileSelect);
uploadForm.addEventListener('submit', handleSubmit);
resetBtn.addEventListener('click', resetForm);

function handleFileSelect(e) {
    const file = e.target.files[0];
    if (file) {
        processFile(file);
    }
}

function processFile(file) {
    // Validation du fichier
    if (!validateFile(file)) return;

    // Mise à jour de l'interface
    updateFileDisplay(file);
    showFileInfo(file);
    hideError();
}

function validateFile(file) {
    // Vérifier le type de fichier
    if (!ACCEPTED_TYPES.includes(file.type)) {
        showError('Type de fichier non supporté. Utilisez JPG, PNG ou GIF.');
        return false;
    }

    // Vérifier la taille
    if (file.size > MAX_FILE_SIZE) {
        showError('Fichier trop volumineux. Maximum 10MB autorisé.');
        return false;
    }

    return true;
}

function updateFileDisplay(file) {
    uploadTitle.textContent = 'Document sélectionné';
    uploadText.textContent = file.name;

    // Aperçu de l'image
    const reader = new FileReader();
    reader.onload = (e) => {
        previewImage.src = e.target.result;
        previewImage.classList.remove('d-none');
    };
    reader.readAsDataURL(file);
}

function showFileInfo(file) {
    fileName.textContent = file.name;
    fileSize.textContent = formatFileSize(file.size);
    fileInfo.style.display = 'block';
}

function formatFileSize(bytes) {
    if (bytes === 0) return '0 Bytes';
    const k = 1024;
    const sizes = ['Bytes', 'KB', 'MB', 'GB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
}

function handleDragOver(e) {
    e.preventDefault();
    uploadBox.classList.add('dragover');
}

function handleDragLeave(e) {
    e.preventDefault();
    uploadBox.classList.remove('dragover');
}

function handleDrop(e) {
    e.preventDefault();
    uploadBox.classList.remove('dragover');
    
    const file = e.dataTransfer.files[0];
    if (file) {
        fileInput.files = e.dataTransfer.files;
        processFile(file);
    }
}

function handleSubmit(e) {
    if (!fileInput.files[0]) {
        e.preventDefault();
        showError('Veuillez sélectionner un fichier avant de continuer.');
        return;
    }

    // Animation de chargement
    submitText.textContent = 'Classification en cours...';
    loadingSpinner.style.display = 'inline-block';
    submitBtn.disabled = true;
    
    // Le formulaire sera soumis normalement au serveur
}

function resetForm() {
    // Reset complet du formulaire
    fileInput.value = '';
    uploadTitle.textContent = 'Glissez-déposez votre document ici';
    uploadText.textContent = 'ou cliquez pour sélectionner un fichier';
    previewImage.classList.add('d-none');
    previewImage.src = '';
    fileInfo.style.display = 'none';
    hideError();
    
    // Reset du bouton submit
    submitText.textContent = 'Classifier le Document';
    loadingSpinner.style.display = 'none';
    submitBtn.disabled = false;
    
    // Si on est sur une page avec des résultats, recharger
    if (document.getElementById('backendResult')) {
        window.location.href = window.location.pathname;
    }
}

function showError(message) {
    errorMessage.textContent = message;
    errorMessage.style.display = 'block';
}

function hideError() {
    errorMessage.style.display = 'none';
}