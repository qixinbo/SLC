// Open the image
path="/home/qixinbo/temp/100X  AWAY FROM FRACTURE 02.tif"
open(path);
title = getTitle();

// Crop
makeRectangle(1, 0, 1023, 687);
run("Crop");

// Auto threshold
setAutoThreshold("Default dark");
setOption("BlackBackground", false);
run("Convert to Mask");

// Invert
run("Invert");

// Remove outliers
run("Remove Outliers...", "radius=1 threshold=1 which=Dark");

// Extract the particles
run("Analyze Particles...", "pixel circularity=0.30-1.00 show=Masks clear");

// Substract
imageCalculator("Subtract create", title,"Mask of " + title);
selectWindow("Result of " + title);

// Invert
run("Invert");

// Watershed
run("Watershed");

// Analyze
run("Analyze Particles...", "size=30-Infinity circularity=0.30-1.00 show=Outlines display clear");
