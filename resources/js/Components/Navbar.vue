<template>
    <nav class="bg-white shadow-md sticky top-0 z-50 transition-all duration-300">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between items-center h-16">
                <div class="flex-shrink-0">
                    <a href="#home" @click="handleNavClick" class="text-2xl font-bold text-customButton hover:text-customdarkblue transition-colors">
                        Pathfinder
                    </a>
                </div>
                
                <!-- Desktop Menu -->
                <div class="hidden md:flex space-x-8">
                    <a 
                        v-for="item in menuItems" 
                        :key="item.name"
                        :href="item.anchor"
                        @click="handleNavClick"
                        class="text-gray-700 hover:text-customButton px-3 py-2 text-sm font-medium transition-colors duration-200"
                        :class="{ 'text-customButton border-b-2 border-customButton': isActive(item.anchor) }"
                    >
                        {{ item.name }}
                    </a>
                </div>

                <!-- Mobile menu button -->
                <div class="md:hidden">
                    <button 
                        @click="mobileMenuOpen = !mobileMenuOpen"
                        class="text-gray-700 hover:text-customButton focus:outline-none focus:text-customButton transition-colors"
                    >
                        <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path v-if="!mobileMenuOpen" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
                            <path v-else stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                        </svg>
                    </button>
                </div>
            </div>
        </div>

        <!-- Mobile Menu -->
        <div 
            v-show="mobileMenuOpen"
            class="md:hidden bg-white border-t border-gray-200 transition-all duration-300"
        >
            <div class="px-2 pt-2 pb-3 space-y-1">
                <a 
                    v-for="item in menuItems" 
                    :key="item.name"
                    :href="item.anchor"
                    @click="handleNavClick"
                    class="block px-3 py-2 text-gray-700 hover:text-customButton hover:bg-blue-gray rounded-md text-base font-medium transition-colors"
                    :class="{ 'text-customButton bg-blue-gray': isActive(item.anchor) }"
                >
                    {{ item.name }}
                </a>
            </div>
        </div>
    </nav>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue';

const mobileMenuOpen = ref(false);
const activeSection = ref('#home');

const menuItems = [
    { name: 'Home', anchor: '#home' },
    { name: 'About', anchor: '#about' },
    { name: 'Objectives', anchor: '#objectives' },
    { name: 'Features', anchor: '#features' },
    { name: 'Methodology', anchor: '#methodology' },
    { name: 'Architecture', anchor: '#architecture' },
    { name: 'Results', anchor: '#results' },
    { name: 'Team', anchor: '#team' },
];

const handleNavClick = (e) => {
    const href = e.currentTarget.getAttribute('href');
    if (href && href.startsWith('#')) {
        e.preventDefault();
        const targetId = href.substring(1);
        const targetElement = document.getElementById(targetId);
        if (targetElement) {
            targetElement.scrollIntoView({ behavior: 'smooth', block: 'start' });
            mobileMenuOpen.value = false;
        }
    }
};

const isActive = (anchor) => {
    return activeSection.value === anchor;
};

const updateActiveSection = () => {
    const sections = menuItems.map(item => item.anchor.substring(1));
    const scrollPosition = window.scrollY + 100; // Offset for sticky navbar

    for (let i = sections.length - 1; i >= 0; i--) {
        const section = document.getElementById(sections[i]);
        if (section && section.offsetTop <= scrollPosition) {
            activeSection.value = `#${sections[i]}`;
            return;
        }
    }
    activeSection.value = '#home';
};

onMounted(() => {
    window.addEventListener('scroll', updateActiveSection);
    updateActiveSection();
});

onUnmounted(() => {
    window.removeEventListener('scroll', updateActiveSection);
});
</script>

