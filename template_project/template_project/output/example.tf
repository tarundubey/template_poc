resource "bigip_ltm_virtual_server" "ec2" {
  name        = "test_vs"
  destination = "10.20.30.40"
  port        = 80
  pool        = "/Common/the-default-pool"
}