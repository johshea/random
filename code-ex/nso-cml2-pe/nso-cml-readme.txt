CML - Import NSO-lab.yaml into CML. All interfaces connected to the bridge are set for dhcp. Based on the network scope for the bridge you may have to adjust the IPs int the nso-env.yml file to allow for proper communication currently they are using 172.16.149.0/24 space. You can also set the interfaces with static IPs and match them in NSO.

NSO - Create Authgroups for CML Lab
	- from the server commandline type: ncs_cli -C -u admin
copy and paste the below:

config
devices authgroup group csrauth
umap admin remote-name cisco remote-password cisco remote-secondary-password cisco
top
devices authgroup group nxosauth
umap admin remote-name cisco remote-password cisco 
top
commit
exit


you can now exit the NCS CLI and run the nso-adddevice.py


make sure you have uploaded the CML lab to CML and adjusted any IP information in the nso-env.py