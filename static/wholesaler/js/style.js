document.addEventListener('DOMContentLoaded', function () {
    var profileIcon = document.querySelector('.profile-icon');

    profileIcon.addEventListener('click', function () {
        var dropdownMenu = document.querySelector('.dropdown-menu');
        dropdownMenu.style.display = (dropdownMenu.style.display === 'block') ? 'none' : 'block';
    });
});