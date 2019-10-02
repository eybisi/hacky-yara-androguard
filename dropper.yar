import "androguard"
import "cuckoo"


rule Anubis : Dropper
{
	meta:
		description = "Anubis Dropper"

	condition:
		androguard.permissions_number < 10 and
		androguard.permission(/REQUEST_INSTALL_PACKAGES/) and
		androguard.permission(/WAKE_LOCK/) and
		androguard.permission(/RECEIVE_BOOT_COMPLETED/) and
		androguard.permission(/ACCESS_NETWORK_STATE/) and	
		androguard.permission(/INTERNET/)
}

rule Anubis2
{

    condition:
        androguard.package_name("com.abdullahbahri.moneyflow")
}
