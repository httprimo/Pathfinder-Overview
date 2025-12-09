<template>
    <MainLayout>
        <div class="bg-white py-16">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <SectionTitle 
                    title="Research Objectives"
                    subtitle="Clear goals and targets for our research project"
                />

                <!-- General Objectives -->
                <section class="mb-16">
                    <div class="bg-indigo-50 rounded-lg p-8 md:p-12 mb-8">
                        <h3 class="text-3xl font-bold text-gray-900 mb-6 flex items-center">
                            <span class="mr-3">🎯</span>
                            General Objectives
                        </h3>
                        <div class="space-y-4">
                            <div class="flex items-start">
                                <div class="flex-shrink-0 w-8 h-8 bg-indigo-600 text-white rounded-full flex items-center justify-center font-semibold mr-4">
                                    1
                                </div>
                                <p class="text-gray-700 text-lg flex-1">
                                    Develop a career and training-matching web application that automatically matches the target career selected by the applicant with training posts that have similar tags. The system will be created using the RAD (Rapid Application Development) model.
                                </p>
                            </div>
                        </div>
                    </div>
                </section>

                <!-- Specific Objectives -->
                <section>
                    <h3 class="text-3xl font-bold text-gray-900 mb-6 flex items-center">
                        <span class="mr-3">📋</span>
                        Specific Objectives
                    </h3>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                        <div class="bg-white border-2 border-gray-200 rounded-lg p-6 hover:border-indigo-500 hover:shadow-lg transition-all duration-300">
                            <div class="flex items-center mb-4">
                                <div class="w-10 h-10 bg-purple-100 rounded-lg flex items-center justify-center mr-3">
                                    <span class="text-purple-600 font-bold">1</span>
                                </div>
                                <h4 class="text-xl font-semibold text-gray-900">Evaluate System Quality</h4>
                            </div>
                            <p class="text-gray-600 mb-3">
                                Evaluate the developed system based on selected ISO/IEC 25010 software quality characteristics:
                            </p>
                            <ul class="text-gray-600 space-y-1 text-sm ml-4">
                                <li>• <strong>Functional Suitability:</strong> System accuracy and completeness</li>
                                <li>• <strong>Compatibility:</strong> Interoperability and co-existence</li>
                                <li>• <strong>Usability:</strong> User experience and learnability</li>
                                <li>• <strong>Security:</strong> Confidentiality and integrity</li>
                                <li>• <strong>Portability:</strong> Adaptability and installability</li>
                            </ul>
                        </div>

                        <div class="bg-white border-2 border-gray-200 rounded-lg p-6 hover:border-indigo-500 hover:shadow-lg transition-all duration-300">
                            <div class="flex items-center mb-4">
                                <div class="w-10 h-10 bg-purple-100 rounded-lg flex items-center justify-center mr-3">
                                    <span class="text-purple-600 font-bold">2</span>
                                </div>
                                <h4 class="text-xl font-semibold text-gray-900">Assess User Perception</h4>
                            </div>
                            <p class="text-gray-600 mb-3">
                                Assess the users' perception of the system's effectiveness using the USE (Usefulness, Satisfaction, and Ease of Use) Questionnaire.
                            </p>
                            <ul class="text-gray-600 space-y-1 text-sm ml-4">
                                <li>• <strong>Usefulness:</strong> Perceived value and capability</li>
                                <li>• <strong>Satisfaction:</strong> User contentment and preference</li>
                                <li>• <strong>Ease of Use:</strong> Simplicity and learnability</li>
                                <li>• <strong>Ease of Learning:</strong> Quick mastery of features</li>
                            </ul>
                        </div>
                    </div>
                </section>
            </div>
        </div>
    </MainLayout>
</template>

<script setup>
import MainLayout from '@/Layouts/MainLayout.vue';
import SectionTitle from '@/Components/SectionTitle.vue';
</script>

