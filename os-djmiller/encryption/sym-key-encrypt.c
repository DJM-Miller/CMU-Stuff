#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <gcrypt.h>

int main(void) {
    if (!gcry_check_version(GCRYPT_VERSION)) {
        fprintf(stderr, "libgcrypt version mismatch\n");
        exit(2);
    }

    // Initialize the library
    if (gcry_control(GCRYCTL_INITIALIZATION_FINISHED_P) == 0) {
        gcry_control(GCRYCTL_ENABLE_M_GUARD);
        gcry_control(GCRYCTL_INITIALIZATION_FINISHED, 0);
    }

    gcry_cipher_hd_t encrypt_handle, decrypt_handle;
    const char *cipher_algo = "AES"; // Change this to your desired algorithm
    int key_length = 16; // Key length for AES-128

    if (gcry_cipher_open(&encrypt_handle, gcry_cipher_map_name(cipher_algo), GCRY_CIPHER_MODE_CBC, 0) != 0) {
        fprintf(stderr, "Failed to open cipher handle for encryption\n");
        exit(2);
    }

    if (gcry_cipher_open(&decrypt_handle, gcry_cipher_map_name(cipher_algo), GCRY_CIPHER_MODE_CBC, 0) != 0) {
        fprintf(stderr, "Failed to open cipher handle for decryption\n");
        exit(2);
    }

    // Set the encryption key
    const char *encryption_key = "\x2b\x7e\x15\x16\x28\xae\xd2\xa6\xab\xf7\x15\x88\x09\xcf\x4f\x3c";
    if (gcry_cipher_setkey(encrypt_handle, encryption_key, key_length) != 0 ||
        gcry_cipher_setkey(decrypt_handle, encryption_key, key_length) != 0) {
        fprintf(stderr, "Failed to set encryption/decryption key\n");
        exit(2);
    }

    const char *plaintext = "Hello World!";
    int plaintext_size = strlen(plaintext); // Excluding null terminator

    // Get block size and calculate padded plaintext size
    size_t block_size = gcry_cipher_get_algo_blklen(GCRY_CIPHER_AES128);
    size_t padded_plaintext_size = (plaintext_size / block_size + 1) * block_size;

    // Allocate memory for padded plaintext and ciphertext
    char *padded_plaintext = (char *)malloc(padded_plaintext_size);
    char *ciphertext = (char *)malloc(padded_plaintext_size);
    if (!padded_plaintext || !ciphertext) {
        fprintf(stderr, "Memory allocation failed\n");
        exit(2);
    }

    // Copy plaintext to padded buffer
    memcpy(padded_plaintext, plaintext, plaintext_size);
    // Pad the rest of the buffer with null bytes
    memset(padded_plaintext + plaintext_size, 0, padded_plaintext_size - plaintext_size);

    // Encrypt the data
    if (gcry_cipher_encrypt(encrypt_handle, ciphertext, padded_plaintext_size, padded_plaintext, padded_plaintext_size) != 0) {
        fprintf(stderr, "Encryption failed\n");
        exit(2);
    }

    printf("Plaintext: %s\n", plaintext);
    printf("Ciphertext: ");
    for (int i = 0; i < padded_plaintext_size; i++) {
        printf("%02X", (unsigned char)ciphertext[i]);
    }
    printf("\n");

    // Decrypt the data
    char *decrypted_text = (char *)malloc(padded_plaintext_size);
    if (!decrypted_text) {
        fprintf(stderr, "Memory allocation failed\n");
        exit(2);
    }

    if (gcry_cipher_decrypt(decrypt_handle, decrypted_text, padded_plaintext_size, ciphertext, padded_plaintext_size) != 0) {
        fprintf(stderr, "Decryption failed\n");
        exit(2);
    }

    printf("Decrypted text: %s\n", decrypted_text);

    // Clean up
    gcry_cipher_close(encrypt_handle);
    gcry_cipher_close(decrypt_handle);
    free(padded_plaintext);
    free(ciphertext);
    free(decrypted_text);

    return 0;
}
