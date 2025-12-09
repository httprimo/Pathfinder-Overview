<template>
    <div class="text-center mb-16 animate-fade-in">
        <div class="inline-block mb-4">
            <span class="text-sm font-semibold text-indigo-600 uppercase tracking-wider">
                {{ title.split(' ')[0] }}
            </span>
        </div>
        <h2 class="text-4xl md:text-5xl lg:text-6xl font-extrabold text-gray-900 mb-6 bg-gradient-to-r from-gray-900 via-gray-800 to-gray-900 bg-clip-text text-transparent">
            {{ title }}
        </h2>
        <div class="flex items-center justify-center mb-6">
            <div class="w-12 h-1 bg-gradient-to-r from-transparent via-customButton to-transparent rounded-full"></div>
            <div class="w-2 h-2 bg-customButton rounded-full mx-2"></div>
            <div class="w-12 h-1 bg-gradient-to-r from-transparent via-customButton to-transparent rounded-full"></div>
        </div>
        <p v-if="subtitle" class="text-gray-600 mt-6 text-lg md:text-xl max-w-3xl mx-auto leading-relaxed">
            {{ subtitle }}
        </p>
    </div>
</template>

<script setup>
defineProps({
    title: {
        type: String,
        required: true
    },
    subtitle: {
        type: String,
        default: ''
    }
});
</script>

<style scoped>
@keyframes fade-in {
    from {
        opacity: 0;
        transform: translateY(-20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.animate-fade-in {
    animation: fade-in 0.6s ease-out;
}
</style>

