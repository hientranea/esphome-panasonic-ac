import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import climate_ir
from esphome.const import CONF_ID

CONF_SUPPORTS_BOTH_SWING = "supports_both_swing"
CONF_SUPPORTS_HORIZONTAL_SWING = "supports_horizontal_swing"
CONF_SUPPORTS_VERTICAL_SWING = "supports_vertical_swing"

AUTO_LOAD = ["climate_ir"]
CODEOWNERS = ["@hientranea"]

panasonic_ns = cg.esphome_ns.namespace("panasonic")
PanasonicClimate = panasonic_ns.class_("PanasonicClimate", climate_ir.ClimateIR)

CONFIG_SCHEMA = climate_ir.CLIMATE_IR_WITH_RECEIVER_SCHEMA.extend(
    {
        cv.GenerateID(): cv.declare_id(PanasonicClimate),
        cv.Optional(CONF_SUPPORTS_HORIZONTAL_SWING, default=False): cv.boolean,
        cv.Optional(CONF_SUPPORTS_VERTICAL_SWING, default=True): cv.boolean,
        cv.Optional(CONF_SUPPORTS_BOTH_SWING, default=False): cv.boolean,
    }
)


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await climate_ir.register_climate_ir(var, config)

    cg.add(
        var.set_supported_swing_modes(
            config[CONF_SUPPORTS_HORIZONTAL_SWING],
            config[CONF_SUPPORTS_VERTICAL_SWING],
            config[CONF_SUPPORTS_BOTH_SWING],
        )
    )
