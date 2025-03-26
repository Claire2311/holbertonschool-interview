/**
* @brief sort by Radix (Radix Sort)
* @param array array of integer
* @param size size of the array
* @return void
*/


void countingSort(int *array, size_t size, int exp) {
    int output[MAX_SIZE]; // Tableau de sortie temporaire
    int count[10] = {0}; // Compteur des occurrences des chiffres

    // Compter le nombre d'occurrences de chaque chiffre
    for (size_t i = 0; i < size; i++) {
        int digit = (array[i] / exp) % 10;
        count[digit]++;
    }

    // Convertir count[] pour qu'il contienne les positions
    for (int i = 1; i < 10; i++) {
        count[i] += count[i - 1];
    }

    // Construire le tableau de sortie
    for (int i = size - 1; i >= 0; i--) {
        int digit = (array[i] / exp) % 10;
        output[count[digit] - 1] = array[i];
        count[digit]--;
    }

    // Copier output[] dans array[]
    for (size_t i = 0; i < size; i++) {
        array[i] = output[i];
    }
}

void radix_sort(int *array, size_t size) {
    if (size == 0) return;
    int max = array[0];
    
    // Trouver la valeur maximale
    for (size_t i = 1; i < size; i++) {
        if (array[i] > max) {
            max = array[i];
        }
    }

    // Appliquer le tri pour chaque position de chiffre
    for (int exp = 1; max / exp > 0; exp *= 10) {
        countingSort(array, size, exp);
        printArray(array, size); // Afficher le tableau après chaque itération
    }
}
