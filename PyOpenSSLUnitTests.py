import unittest
from CertCheck import CertificateChecker
from test_certs import (
    int_ca_cert_pem,
    root_ca_cert_pem,
    good_leaf_cert_pem,
    bad_leaf_cert_pem
)
from OpenSSL.crypto import (
    X509Store,
    load_certificate,
    FILETYPE_PEM
)


class TestCertificateChecker(unittest.TestCase):
    def test_good_leaf_cert(self):
        check = CertificateChecker(good_leaf_cert_pem)
        self.assertTrue(check.verify_cert(), "Expected good leaf to Verify")

    def test_bad_leaf_cert(self):
        check = CertificateChecker(bad_leaf_cert_pem)
        self.assertFalse(check.verify_cert(), "Expected bad leaf to fail Verify")

    def test_no_int_ca_in_trust_store(self):
        check = CertificateChecker(good_leaf_cert_pem)
        check.trusted_certs = X509Store()       # re-init Trust Store
        root_cert = load_certificate(FILETYPE_PEM, root_ca_cert_pem)
        check.trusted_certs.add_cert(root_cert)
        self.assertFalse(check.verify_cert(), "Expected to fail verify, as Int CA was removed")

    def test_partial_chain_allowed(self):
        check = CertificateChecker(good_leaf_cert_pem)
        check.trusted_certs = X509Store()       # re-init Trust Store
        check.trusted_certs.set_flags(0x80000)  # X509_V_FLAG_PARTIAL_CHAIN
        int_cert = load_certificate(FILETYPE_PEM, int_ca_cert_pem)
        check.trusted_certs.add_cert(int_cert)
        self.assertTrue(check.verify_cert(), "Expected OK. No Root CA. Int CA {0} . + flag for Partial Chain flag".format(int_cert))

    def test_openssl_types(self):
        check = CertificateChecker(bad_leaf_cert_pem)
        self.assertTrue(isinstance(check.trusted_certs, OpenSSL.crypto.X509Store))
        self.assertTrue(isinstance(check.untrusted_leaf, OpenSSL.crypto.X509))
