/*
Template Name: ShopGrids - Bootstrap 5 eCommerce HTML Template.
Author: GrayGrids
*/

// Tab Switching Functionality
const tabs = document.querySelectorAll('.tab-link');
const tabSections = document.querySelectorAll('.tab-section');

tabs.forEach(tab => {
tab.addEventListener('click', () => {
    // Remove 'active' class from all tabs and tab sections
    tabs.forEach(t => t.classList.remove('active'));
    tabSections.forEach(section => section.classList.remove('active'));

    // Add 'active' class to clicked tab and corresponding section
    tab.classList.add('active');
    const tabId = tab.getAttribute('data-tab');
    document.getElementById(tabId).classList.add('active');
});
});