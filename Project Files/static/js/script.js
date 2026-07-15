/**
 * script.js
 * Lightweight client-side validation for the OptiCrop prediction form.
 */

(function () {
    "use strict";

    const NON_NEGATIVE_FIELDS = ["N", "P", "K", "humidity", "ph", "rainfall"];

    document.addEventListener("DOMContentLoaded", function () {
        const form = document.getElementById("cropForm");

        if (!form) {
            return;
        }

        form.addEventListener("submit", function (event) {
            const fields = form.querySelectorAll("input[type='number']");
            let errorMessage = "";

            fields.forEach(function (field) {
                const rawValue = field.value.trim();

                if (rawValue === "") {
                    errorMessage = "Please fill in all fields before submitting.";
                    return;
                }

                const numericValue = parseFloat(rawValue);

                if (isNaN(numericValue)) {
                    errorMessage = "All fields must contain valid numeric values.";
                    return;
                }

                if (NON_NEGATIVE_FIELDS.includes(field.id) && numericValue < 0) {
                    errorMessage = `${field.id} cannot be a negative value.`;
                }
            });

            if (errorMessage !== "") {
                event.preventDefault();
                window.alert(errorMessage);
            }
        });
    });
})();