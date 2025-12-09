<?php

use App\Http\Controllers\ResearchController;
use Illuminate\Support\Facades\Route;
use Inertia\Inertia;

Route::get('/', [ResearchController::class, 'home'])->name('home');
Route::get('/about', function () {
    return redirect('/#about');
})->name('about');
Route::get('/objectives', function () {
    return redirect('/#objectives');
})->name('objectives');
Route::get('/features', function () {
    return redirect('/#features');
})->name('features');
Route::get('/methodology', function () {
    return redirect('/#methodology');
})->name('methodology');
Route::get('/architecture', function () {
    return redirect('/#architecture');
})->name('architecture');
Route::get('/results', function () {
    return redirect('/#results');
})->name('results');
Route::get('/team', function () {
    return redirect('/#team');
})->name('team');

