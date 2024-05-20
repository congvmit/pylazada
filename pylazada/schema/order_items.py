from typing import Dict, List, Optional

from pydantic import BaseModel


class PickUpStoreInfo(BaseModel):
    pick_up_store_address: str
    pick_up_store_name: str
    pick_up_store_open_hour: List[str]
    pick_up_store_code: str


class Data(BaseModel):
    pick_up_store_info: PickUpStoreInfo
    tax_amount: str
    reason: str
    sla_time_stamp: str
    show_giftwrapping_tag: str
    voucher_seller: str
    purchase_order_id: str
    payment_time: str
    voucher_code_seller: str
    voucher_code: str
    package_id: str
    buyer_id: str
    variation: str
    product_id: str
    voucher_code_platform: str
    purchase_order_number: str
    sku: str
    gift_wrapping: str
    order_type: str
    invoice_number: str
    show_personalization_tag: str
    cancel_return_initiator: str
    shop_sku: str
    is_reroute: str
    stage_pay_status: str
    sku_id: str
    tracking_code_pre: str
    order_item_id: str
    shop_id: str
    order_flag: str
    is_fbl: str
    name: str
    delivery_option_sof: str
    order_id: str
    fulfillment_sla: str
    status: str
    paid_price: str
    product_main_image: str
    voucher_platform: str
    product_detail_url: str
    warehouse_code: str
    promised_shipping_time: str
    shipping_type: str
    created_at: str
    voucher_seller_lpi: str
    shipping_fee_discount_platform: str
    personalization: str
    wallet_credits: str
    updated_at: str
    currency: str
    shipping_provider_type: str
    voucher_platform_lpi: str
    shipping_fee_original: str
    is_digital: str
    item_price: str
    shipping_service_cost: str
    tracking_code: str
    shipping_fee_discount_seller: str
    shipping_amount: str
    reason_detail: str
    return_status: str
    shipment_provider: str
    priority_fulfillment_tag: str
    voucher_amount: str
    digital_delivery_info: str
    extra_attributes: str


class ResponseOrderItems(BaseModel):
    code: str
    data: Optional[List[Data]]
    request_id: str
