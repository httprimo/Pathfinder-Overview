<template>
    <div class="w-full bg-gradient-to-br from-purple-50 via-blue-50 to-indigo-50 min-h-screen py-8">
        <!-- Header with Step Indicator and Navigation -->
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mb-8">
            <div class="flex items-center justify-between">
                <div class="flex items-center gap-4">
                    <div class="bg-customButton text-white px-4 py-2 rounded-full font-semibold text-sm">
                        Step {{ currentStep + 1 }} of {{ totalSteps }}
                    </div>
                    <span class="text-gray-500 text-sm">{{ currentStepData.title || 'System Screenshot' }}</span>
                </div>
                <div class="flex items-center gap-2">
                    <button
                        @click="previousStep"
                        :disabled="currentStep === 0"
                        class="w-10 h-10 rounded-full bg-white border border-gray-300 flex items-center justify-center hover:bg-gray-50 disabled:opacity-50 disabled:cursor-not-allowed transition-all"
                        :class="{ 'cursor-not-allowed': currentStep === 0 }"
                    >
                        <svg class="w-5 h-5 text-gray-700" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" />
                        </svg>
                    </button>
                    <button
                        @click="nextStep"
                        :disabled="currentStep === totalSteps - 1"
                        class="w-10 h-10 rounded-full bg-white border border-gray-300 flex items-center justify-center hover:bg-gray-50 disabled:opacity-50 disabled:cursor-not-allowed transition-all"
                        :class="{ 'cursor-not-allowed': currentStep === totalSteps - 1 }"
                    >
                        <svg class="w-5 h-5 text-gray-700" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
                        </svg>
                    </button>
                </div>
            </div>
        </div>

        <!-- Main Content Area -->
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 items-center">
                <!-- Left Panel - Screenshot Display -->
                <div class="bg-gradient-to-br from-purple-100 to-indigo-100 rounded-2xl p-8 shadow-xl">
                    <div class="bg-white rounded-lg overflow-hidden shadow-lg">
                        <img
                            :src="currentStepData.image"
                            :alt="currentStepData.title || `Step ${currentStep + 1}`"
                            class="w-full h-auto"
                            @error="handleImageError"
                        />
                    </div>
                </div>

                <!-- Right Panel - Description -->
                <div class="space-y-4">
                    <h2 class="text-4xl font-bold text-customButton mb-4">
                        {{ currentStepData.title || `Step ${currentStep + 1}` }}
                    </h2>
                    <p class="text-gray-600 text-lg leading-relaxed">
                        {{ currentStepData.description || 'System screenshot showing key functionality.' }}
                    </p>
                    <div v-if="currentStepData.details" class="mt-6 space-y-2">
                        <h3 class="text-xl font-semibold text-gray-800">Key Features:</h3>
                        <ul class="list-disc list-inside space-y-1 text-gray-600">
                            <li v-for="(detail, index) in currentStepData.details" :key="index">{{ detail }}</li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>

        <!-- Pagination Dots and Progress Bar -->
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mt-12">
            <!-- Pagination Dots -->
            <div class="flex justify-center items-center gap-3 mb-4 flex-wrap">
                <button
                    v-for="(step, index) in steps"
                    :key="index"
                    @click="goToStep(index)"
                    class="w-10 h-10 rounded-full border-2 flex items-center justify-center font-semibold text-sm transition-all"
                    :class="index === currentStep 
                        ? 'bg-customButton text-white border-customButton' 
                        : 'bg-white text-gray-700 border-gray-300 hover:border-customButton hover:bg-purple-50'"
                >
                    {{ index + 1 }}
                </button>
            </div>

            <!-- Progress Bar -->
            <div class="w-full max-w-4xl mx-auto">
                <div class="h-2 bg-gray-200 rounded-full overflow-hidden">
                    <div
                        class="h-full bg-customButton transition-all duration-300 ease-out"
                        :style="{ width: `${((currentStep + 1) / totalSteps) * 100}%` }"
                    ></div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';

const props = defineProps({
    steps: {
        type: Array,
        required: true,
        default: () => []
    }
});

const currentStep = ref(0);

const totalSteps = computed(() => props.steps.length);

const currentStepData = computed(() => {
    return props.steps[currentStep.value] || {};
});

const nextStep = () => {
    if (currentStep.value < totalSteps.value - 1) {
        currentStep.value++;
    }
};

const previousStep = () => {
    if (currentStep.value > 0) {
        currentStep.value--;
    }
};

const goToStep = (index) => {
    if (index >= 0 && index < totalSteps.value) {
        currentStep.value = index;
    }
};

const handleImageError = (event) => {
    // Fallback to placeholder if image fails to load
    event.target.src = 'data:image/svg+xml,%3Csvg xmlns="http://www.w3.org/2000/svg" width="800" height="600"%3E%3Crect fill="%23f3f4f6" width="800" height="600"/%3E%3Ctext x="50%25" y="50%25" dominant-baseline="middle" text-anchor="middle" font-family="Arial" font-size="24" fill="%239ca3af"%3EScreenshot not found%3C/text%3E%3C/svg%3E';
};

// Keyboard navigation
onMounted(() => {
    const handleKeyPress = (e) => {
        if (e.key === 'ArrowLeft') {
            previousStep();
        } else if (e.key === 'ArrowRight') {
            nextStep();
        }
    };
    window.addEventListener('keydown', handleKeyPress);
    
    return () => {
        window.removeEventListener('keydown', handleKeyPress);
    };
});
</script>

<style scoped>
/* Smooth transitions */
.transition-all {
    transition-property: all;
    transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
    transition-duration: 300ms;
}
</style>

