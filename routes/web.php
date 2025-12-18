<?php

use App\Http\Controllers\ResearchController;
use Illuminate\Support\Facades\Route;
use Inertia\Inertia;

Route::get('/', [ResearchController::class, 'home'])->name('home');
Route::get('/about', function () {
    return redirect('/#about');
})->name('about');
Route::get('/features', function () {
    return redirect('/#features');
})->name('features');
Route::get('/team', function () {
    return redirect('/#team');
})->name('team');

